import pydicom
from pydicom import dcmread
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import pydicom
import time

class Dicom_Loader_Class:
    def timeit(func):
        def wrapper(*args, **kwargs):
            """Wrapper function used for timing functions

            Returns:
                result (string): elapsed time in seconds for how long a function takes to run
            """
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            elapsed = end - start
            print(f'Time taken: {elapsed:.6f} seconds')
            return result
        return wrapper
    
    @timeit
    def fDicom_Reader(dcm_filepaths):
        """Accepts only dicom file types, reads them and scales them according to header information

        Args:
            dcm_filepaths strings: filepaths pointing to dicom files

        Returns:
            MxNxZ image array: scaled image array (CT Images)
        """
        try:
            images = [dcmread(i) for i in dcm_filepaths]
        except:
            pass
        dcm_imgs = np.stack([i.pixel_array.astype('float32') + i.RescaleIntercept for i in images])
        return dcm_imgs

    @timeit
    def fFolder_Selection():
        """
        The function `folder_select` opens a dialog box for selecting a folder location in a Python
        program.
        """
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        folder_location = askdirectory() # show an "Open" dialog box and return the path to the selected folder
        return folder_location

    @timeit
    def fRecursive_Dicom_File_Find(input_path,dicom_filepaths):
        """
        The function recursively navigates through folders to find DICOM files and stores their file
        paths.
        
        :param new_path: The `new_path` parameter in the `recursive_folder_navigation` method is a
        string representing the path to a directory that you want to navigate recursively. The method
        iterates over the contents of this directory and performs certain actions based on whether the
        content is a subdirectory or a DICOM file
        """
        for filename in os.listdir(input_path):
            if os.path.isdir(os.path.join(input_path,filename)):
                fRecursive_Dicom_File_Find(os.path.join(input_path,filename),dicom_filepaths)
            elif pydicom.misc.is_dicom(os.path.join(input_path,filename)):
                dicom_filepaths.append(os.path.join(input_path,filename))
        return dicom_filepaths