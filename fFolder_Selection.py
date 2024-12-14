from tkinter import Tk
from tkinter.filedialog import askdirectory

def fFolder_Selection():
    """
    The function `folder_select` opens a dialog box for selecting a folder location in a Python
    program.
    """
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    folder_location = askdirectory() # show an "Open" dialog box and return the path to the selected folder
    return folder_location