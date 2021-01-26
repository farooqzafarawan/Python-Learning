import os
import tkinter as tk
#from tkinter import filedialog
from gooey import Gooey, GooeyParser


#tkroot = tk.Tk()  # Initializing Tkinter
#workingDir = filedialog.askdirectory(parent=tkroot,initialdir="/",title='Please select a directory')
#workingDir = r'F:\TV MEDIA\Dirilis Ertugrul\Season 2'
#fileList = os.listdir(workingDir)

# firstSplit = 'Module_'
# secondSplit = '_SUB'

@Gooey(program_name="Rename Files in Folder")
def renameFiles():
    parser = GooeyParser(description='Create Quarterly Marketing Report')
    parser.add_argument('data_directory',
                        action='store',
                        widget='DirChooser',
                        help="Source directory that contains files")
    parser.add_argument('FirstSplitPattern', help="First Pattern to split file Name")
    parser.add_argument('SecondSplitPattern', help="Second Pattern to split file Name") 
    parser.add_argument('PrintFileName', help="Indicator for just printing the new name instead of rename file") 
    
    args = parser.parse_args()

    workingDir = args.data_directory
    firstSplit = args.FirstSplitPattern
    secondSplit = args.SecondSplitPattern
    printNameOnly = args.PrintFileName

    # Traverse root directory, and list directories as dirs and files as files
    for root, dirs, fileList in os.walk(workingDir):
        os.chdir( root )
        path = root.split(os.sep)
        print((len(path) - 1) * '***', os.path.basename(root))
        
        for filename in fileList:
            fname, ext = os.path.splitext(filename)


            if firstSplit in fname:
                fileSplit1 = fname.split(firstSplit)[1]
                if secondSplit != '':
                    mainName = fileSplit1.split(secondSplit)[0] #main file name
                else:
                    mainName = fileSplit1
                
                newname = mainName.strip() + ext
                print(len(path) * '...', newname)

                if printNameOnly == 'YES':
                    print(newname)
                else:
                    os.rename(filename, newname)
            else:
                print(f'Could not find Characters {firstSplit} or {secondSplit} in {filename}')

if __name__ == "__main__":
    renameFiles()
