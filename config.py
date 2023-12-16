import os
from yacs.config import CfgNode

_C = CfgNode()

_C.DATASET_DIR = '/content/DETR-Car-Logo-Detection/Car_Logo_Dataset'
_C.IMAGE_DIR = os.path.join(_C.DATASET_DIR, 'Car_Logo_Dataset_V_5_Images')
_C.ANNOT_FILE = os.path.join(
    _C.DATASET_DIR, 'Car Logo Dataset V-5 Annotations DETR.txt')
_C.CROPPED_ANNOT_FILE = os.path.join(
    _C.DATASET_DIR, 'Car Logo Dataset V-5 Training Set Annotations Cropped.txt')
_C.CROPPED_ANNOT_FILE_TEST = os.path.join(
    _C.DATASET_DIR, 'Car Logo Dataset V-5 Test Set Annotations Cropped.txt')

_C.CLASS_NAMES = ['Audi', 'Chrysler', 'Citroen', 'GMC', 'Honda', 'Hyundai', 'Infiniti', 'Mazda', 'Mercedes', 'Mitsubishi', 
                  'Nissan', 'Renault', 'Toyota', 'Volkswagen', 'acura', 'bmw', 'cadillac', 'chevrolet', 'dodge', 'ford', 'jeep', 
                  'kia', 'lexus', 'license-plate', 'lincoln', 'mini', 'porsche', 'ram', 'range-rover', 'skoda', 'subaru', 'suzuki', 'volvo']


def get_cfg_defaults():
    return _C.clone()
