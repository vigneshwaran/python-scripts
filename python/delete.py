import sys
import os,shutil
from os import listdir


directory = "C:\\Users\\Vigneshwaraen\\Desktop\\01_introduction\\"
for folderName, subfolders, filenames in os.walk(directory):
        for subfolder in subfolders:

            test = listdir(directory+subfolder)
            for item in test:
                if item.endswith(".mp4"):
                    shutil.move(os.path.join(directory, item),"C:\\Users\\Vigneshwaraen\\Desktop\\new")
                else:
                    #os.remove(os.path.join(directory, item))
                    os.rmdir(subfolder)