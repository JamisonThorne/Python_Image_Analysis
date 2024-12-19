# import os
# import numpy as np
# from tkinter import Tk
# from tkinter.filedialog import askdirectory
# import pydicom
# from pydicom import dcmread
# import fFolder_Selection
# import Dicom_Loader
import numpy as np
from Dicom_Loader import Dicom_Loader_Class as DLC 
from ROI_Selection import ROI_Selection_Class as SLC 
from Figure_Generation import Figure_Generation_Class as FGC 
import random

def main():
    """
    The main purpose of this script is twofold
    1. To showcase various tools I have made for image analysis
    2. A generalizable functional library for future implementation
    """
    selected_folder = DLC.fFolder_Selection()   # gui for selecting folders that contain dicom images
    dicom_filepaths = DLC.fRecursive_Dicom_File_Find(selected_folder,[]) # recursively pull dicom filepaths
    image_ds = DLC.fDicom_Reader(dicom_filepaths) # using the collection of filepaths, read dicom information using pydicom
    ########################
    center = (round(np.shape(image_ds)[1]/2),round(np.shape(image_ds)[2]/2))
    radius = 100
    ########################
    if len(np.shape(image_ds))==3:  # if image_ds has 3dimensions, send to 3D function. There are better ways to do this
        mask = SLC.f3D_Circle_Mask_Generator(image_ds,center,radius)
    elif len(np.shape(image_ds))==2: # if image_ds has 2dimensions, send to 2D function. There are better ways to do this
        mask = SLC.f2D_Circle_Mask_Generator(image_ds,center,radius)
    print(SLC.fImage_Mask_Mean(image_ds,mask))  # mean for masked region
    print(SLC.fImage_Mask_Std(image_ds,mask))   # std for masked region
    random_slice = image_ds[round(random.random()*100)][:][:]
    FGC.fCircle_Draw_Figure(random_slice,center,radius,40,400)
    
if __name__ == '__main__':
    main()