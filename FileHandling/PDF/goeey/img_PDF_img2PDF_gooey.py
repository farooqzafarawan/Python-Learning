import os
import img2pdf
from tkinter import filedialog , Tk
from gooey import Gooey, GooeyParser
from pathlib import Path    


# tkroot = Tk()  # Initializing Tkinter
# outDir = filedialog.askdirectory(parent=tkroot, initialdir="/", title='Please select a directory')

# # convert all files ending in .jpg inside a directory
# outDir = r"C:\URDU\eBooks\RekhtaDownload"
# outFile = os.path.join(outDir, "Tuzk-e-Urdu.pdf")

#dirname = r"C:\URDU\eBooks\RekhtaDownload\Tuzk-e-Urdu"


@Gooey(program_name="Images combined as PDF")
def extractPages():
    parser = GooeyParser(description='Create Quarterly Marketing Report')
    parser.add_argument('work_dir',
                        action='store',
                        widget='DirChooser',
                        help="Output directory for PDF file")
    parser.add_argument('img_dir',
                        action='store', widget='DirChooser', help="Source directory for image files")
    parser.add_argument('fileName', help='Enter name for New PDF file')    
    parser.add_argument('startPage', help="First page to start extraction")
    parser.add_argument('endPage', help="Last page to start extraction")

    args = parser.parse_args()
    outDir = args.work_dir
    imageDir = args.img_dir
    pdfName= args.fileName
    pgStart = int(args.startPage)
    pgEnd = int(args.endPage)

    ext = '.pdf'
    fileConcat = f'{pdfName}_{pgStart}_{pgEnd}{ext}'
    print(fileConcat)
    outFile = os.path.join(outDir, fileConcat)
    print(outFile)

    with open(outFile,"wb") as f:
        imgs = []
        
        for fname in os.listdir(imageDir):
            if not fname.endswith(".jpg"):
                continue
            pgNum, ext = fname.split('.')
            pageNum = int(pgNum)
            if (pageNum >= pgStart and pageNum <= pgEnd ):
                path = os.path.join(imageDir, fname)
                print(path)
                imgs.append(path)
                
                if os.path.isdir(path):
                    continue
        for img in imgs:
            print(img)    
        f.write(img2pdf.convert(imgs))


extractPages()

print('Program Ended')