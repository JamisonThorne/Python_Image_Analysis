import os
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askdirectory
import pydicom
from pydicom import dcmread

def main(): 
    selected_folder = fFolder_Selection()
    dicom_filepaths = fRecursive_Dicom_File_Find(selected_folder,[])
    dicom_images = fLoad_Dicoms(dicom_filepaths)

if __name__ == '__main__':
    main()