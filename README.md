# object_detector
A Django web app with MaskRCNN model for object detection and segementation. Developed for gsoc 2020 code challenge

Place the weights for MaskRCNN inside detector/saved_models.
https://download.pytorch.org/models/maskrcnn_resnet50_fpn_coco-bf2d0c1e.pth

![alt text](https://github.com/droidLight/object_detector/blob/master/sample_pic_1.png)
![alt text](https://github.com/droidLight/object_detector/blob/master/sample_pic_2.png)

# Installation:
1. Create an virtual env or conda environment.(optional)
2. clone the repo and install dependencies listed in requirements.txt by 'pip install -r requirements.txt'
3. Copy the weights of the model into object_detector/object_detector/detector/saved_models/
4. To start a local webserver run, 'python manage.py runserver'
The app can be now accessed via browser on http://localhost:8000/ (by default)

