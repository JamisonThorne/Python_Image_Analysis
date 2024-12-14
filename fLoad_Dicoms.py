import pydicom
from pydicom import dcmread
import numpy as np

def fLoad_Dicoms(dcm_filepaths):
    """
    The function `load_dicom_images` reads DICOM files and stacks their pixel arrays as float32
    arrays.
    """
    try:
        images = [dcmread(i) for i in dcm_filepaths]
    except:
        pass
    dcm_imgs = np.stack([i.pixel_array.astype('float32') + i.RescaleIntercept for i in images])
    return dcm_imgs