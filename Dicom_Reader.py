import os
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askdirectory
import pydicom
from pydicom import dcmread

def main(): 
    image_tool = Dicom_Reader()
    image_tool.image_hub()

class Dicom_Reader:
    """
    Reads DICOM files for processing, which are commonly used in medical imaging.
    """
    def __init__(self):
        self.dcm_filepath = []
        self.dcm_imgs = []
        
    def image_hub(self):
        """
        This Python function navigates through folders to find DICOM images and loads them for further
        processing.
        :return: The `image_hub` method is returning the loaded DICOM images (`self.dcm_imgs`).
        """
        self.folder_select()
        self.recursive_folder_navigation(self.folder_location)
        if len(self.dcm_filepath) == 0:
            print("No dicom images found")
            return
        self.load_dicom_images()
        return self.dcm_imgs
        
    def load_dicom_images(self):
        """
        The function `load_dicom_images` reads DICOM files and stacks their pixel arrays as float32
        arrays.
        """
        try:
            images = [dcmread(i) for i in self.dcm_filepath]
        except:
            pass
        self.dcm_imgs = np.stack([i.pixel_array.astype('float32') + i.RescaleIntercept for i in images])
    
    def recursive_folder_navigation(self,new_path):
        """
        The function recursively navigates through folders to find DICOM files and stores their file
        paths.
        
        :param new_path: The `new_path` parameter in the `recursive_folder_navigation` method is a
        string representing the path to a directory that you want to navigate recursively. The method
        iterates over the contents of this directory and performs certain actions based on whether the
        content is a subdirectory or a DICOM file
        """
        for filename in os.listdir(new_path):
            if os.path.isdir(os.path.join(new_path,filename)):
                self.recursive_folder_navigation(os.path.join(new_path,filename))
            elif pydicom.misc.is_dicom(os.path.join(new_path,filename)):
                self.dcm_filepath.append(os.path.join(new_path,filename))

    def folder_select(self):
        """
        The function `folder_select` opens a dialog box for selecting a folder location in a Python
        program.
        """
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        self.folder_location = askdirectory() # show an "Open" dialog box and return the path to the selected folder

if __name__ == '__main__':
    main()