import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('')
    model.val(data='',
              split='test',
              imgsz=640,
              batch=32,
              # rect=False,
              # save_json=True, # if you need to cal coco metrice
              project='runs/test',
              name='',
              )