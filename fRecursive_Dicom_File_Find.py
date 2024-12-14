import os
import pydicom

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