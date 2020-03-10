from django.apps import AppConfig
import torch
from torchvision.models.detection.backbone_utils import resnet_fpn_backbone
from torchvision.models.detection.mask_rcnn import MaskRCNN

class DetectorConfig(AppConfig):
    name = 'detector'

    #load model
    model_path = 'detector/saved_models/maskrcnn_resnet50_fpn_coco-bf2d0c1e.pth'
    backbone = backbone = resnet_fpn_backbone('resnet50', False)
    maskRCNNModel = MaskRCNN(backbone, 91)
    checkpoint = torch.load(model_path)
    maskRCNNModel.load_state_dict(checkpoint)
    maskRCNNModel.eval()
    print("Model Loaded")

    
