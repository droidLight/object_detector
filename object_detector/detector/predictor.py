from .apps import DetectorConfig
import numpy as np
import cv2 as cv
import torch
from object_detector import settings
from .models import ImageModel
import os
import shutil

def apply_bounds_masks(image_path, threshold, output_name):
    image = cv.imread(settings.BASE_DIR + image_path, -1)

    #preprocessing and converting to torch tensor
    print(f"Image shape: {image.shape} type: {type(image)}")
    img = np.asarray(image)
    img = img.transpose(-1, 0, 1)
    img = img/255
    img = torch.from_numpy(img).float()
    print("proccessed")
    model = DetectorConfig.maskRCNNModel
    pred = model([img])

    #obtaining score greater than given threshold value
    pred_scores = pred[0]['scores']
    high_scores = [i for i in range(len(pred_scores)) if pred_scores[i] > threshold]

    
    #converting tensors to numpy array and selecting the predictions which satifies threshold 
    pred_boxes = pred[0]['boxes'].detach().numpy()
    pred_boxes = pred_boxes[high_scores]
    pred_masks = (pred[0]['masks'] > 0.5).squeeze().detach().numpy()
    pred_masks = pred_masks[high_scores]

    #applying bounding boxes and masks on original image
    #creating RGB masks for visualization
    r = np.zeros_like(pred_masks[0]).astype(np.int32)
    g = np.zeros_like(pred_masks[0]).astype(np.int32)
    b = np.zeros_like(pred_masks[0]).astype(np.int32)
    
    maskedImage = image.copy()
    croppedList = list()

    for box, mask in zip(pred_boxes, pred_masks):
        #creating RGB masks and overlaying on the image along with boundaries
        r[mask == 1], g[mask == 1], b[mask == 1] = [0, 255, 0]
        mask_rgb = np.dstack([r,g,b])
        maskedImage = cv.addWeighted(maskedImage.astype(np.int32), 1, mask_rgb.astype(np.int32), 0.7, 0)
        #cv.rectangle(maskedImage, (box[0], box[1]), (box[2], box[3]), (0, 0, 255))

        #cropping detected objects
        r[mask == 1], g[mask == 1], b[mask == 1] = [255, 255, 255]
        mask_rgb = np.dstack([r,g,b])
        croppedList.append(cv.bitwise_and(image.astype(np.int32), mask_rgb.astype(np.int32)))
        r.fill(0), g.fill(0), b.fill(0)

    #create directory to save the images
    image_path ="/media/masked_images/"+output_name
    if os.path.exists(settings.BASE_DIR + image_path):
        shutil.rmtree(settings.BASE_DIR + image_path)
    os.makedirs(settings.BASE_DIR + image_path)
    
    #save the image with mask applied
    maskedImagePath = image_path + "/applied_masks.jpeg"
    cv.imwrite(settings.BASE_DIR + maskedImagePath, maskedImage)
    print("Image saved")

    #save cropped image
    croppedListURL = list()
    for i, cropped in enumerate(croppedList):
        croppedImagePath = image_path + "/cropped_"+str(i)+".jpeg"
        croppedListURL.append(croppedImagePath)
        cv.imwrite(settings.BASE_DIR + croppedImagePath, cropped)
    print("Saved masks")

    return maskedImagePath, croppedListURL


