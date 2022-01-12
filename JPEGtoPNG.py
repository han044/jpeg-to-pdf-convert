'''
Add Any Number of Images in the input folder, it will auto-create "converted" directory and copy converted files into it.
Note: This will only work when folder is selected. modify accordingly
'''

import os
import sys
from PIL import Image


def convertImageToPng():
    print(" \n\n converting to PNG format ... ")
    img_list = os.listdir(ex_fold)
    if(len(img_list) == 0):
        print("Images not given in the input file...")
        return

    for index in img_list:
        img = Image.open(f"./{ex_fold}/{index}")
        clean_name = os.path.splitext(index)[0]
        img.save(f"./{new_fold}/{clean_name}-converted.png")


ex_fold = "input"
new_fold = "converted"


if not os.path.exists(new_fold):
    print("\n Creating Directory \"converted\" ")
    os.makedirs(new_fold)

convertImageToPng()
