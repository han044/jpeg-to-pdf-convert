import os
import sys
from PIL import Image


def convertImageToPng():
    '''i points to the current index to disallow file replacement'''
    i = len(os.listdir(new_fold)) + 1
    for index in os.listdir(ex_fold):
        img = Image.open("./" + ex_fold + "/" + index)
        print(index)
        print(" \n\n Converting to png... \n")
        img.save("./new/img"+str(i)+".png")
        i = i + 1


try:
    ex_fold = sys.argv[1]
    new_fold = sys.argv[2]
except IndexError as err:
    print(" \n\n Pls Give Input... ")
    exit()

try:
    os.mkdir(new_fold)
except FileExistsError:
    print("\n\n Folder Already exists! ")


print("\n Converting to Png...")
convertImageToPng()
