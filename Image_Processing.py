# import os
# import numpy as np
# from tkinter import Tk
# from tkinter.filedialog import askdirectory
# import pydicom
# from pydicom import dcmread
# import fFolder_Selection
# import Dicom_Loader
from Dicom_Loader import Dicom_Loader_Class as DLC 

def main(): 
    selected_folder = DLC.fFolder_Selection()
    dicom_filepaths = DLC.fRecursive_Dicom_File_Find(selected_folder,[])
    dicom_images = DLC.fLoad_Dicoms(dicom_filepaths)

if __name__ == '__main__':
    main()