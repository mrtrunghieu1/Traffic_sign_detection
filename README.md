# Traffic_sign_detection
> Traffic Sign Detection in Zalo Challenge competition

## Table of contents
  - [Enviroments](#Enviroments)
  - [Train On Custom Data](#train_data)
  - [Imputation Methods](#imputation-methods)
  - [Classification Algorithm](#classification-algorithm)
  - [Contact](#contact)


## Enviroments
* Ubuntu 
```bash
    pip install -r requirements.txt
```

## Train On Custom Data

Followed by github: 
>https://github.com/ultralytics/yolov3?fbclid=IwAR1EKN08md9W9h1OD3SxrG_nRUlWnsTp9wnR7NBQK_1IWGWEyQoiM50Q9Ls

* Tutorials -> Train Custom Data

* Create folder: 
    + data/images
	+ data/labels

* Copy all images from traffic_train to images

* Create /labels/*.txt: 
```bash
cd pre_processing
python pre_processing.py --create_labels_txt True
```

* Create coco.names: (Save as data/coco.names)
```bash
cam_nguoc_chieu
cam_dung_va_do
cam_re
gioi_han_toc_do
cam_con_lai
nguy_hiem
hieu_lenh
```

* Create Train and Validation:
```bash
python pre_processing.py --create_train_txt True
```

* Create coco16.data (Save as data/coco16.data):
```bash
classes=7
train=train.txt
valid=val.txt
names=data/coco.names
```

* Update yolov3-spp.cfg:
```bash
filters = 32 <(5 + 7)*3>
classes = 7
```

* When config done then push code on sever:
> Run Code
```bash
python train.py --cfg cfg/yolov3-spp.cfg --data data/coco16.data --weights '' --device 2 --batch-size 8
```
> Visualiaztion on tensorboard
```bash
tensorboard --host 192.168.54.158 --port 8003 --logdir runs/
```
> Predict Output
* Edit detect.py follow format public_sample_submission in Zalo competition
* weight = 'best.pt' when training 4500 images
```bash
python detect.py --source data/samples/traffic_public_test/images --cfg cfg/yolov3-spp.cfg --weights weights/best.pt --names data/coco.names --device 1 --save-txt
```

