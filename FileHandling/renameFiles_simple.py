import os
from tkinter import filedialog

import os

workingDir = r'C:\MEDIA\TV\MrRobot'

splitChar = '.'
#secondsplit = ''

# Traverse root directory, and list directories as dirs and files as files
for root, _, fileList in os.walk(workingDir):
    path = root.split(os.sep)

    for fname in fileList:
        fname, ext = os.path.splitext(fname)

        mainName = fname.split(splitChar)  # main file name
        print(mainName)
        newname = str(mainName[2]) + '_' + str(mainName[1]) + ext
        lenpath = len(path) * '..'
        print(f'{lenpath} {newname}')

