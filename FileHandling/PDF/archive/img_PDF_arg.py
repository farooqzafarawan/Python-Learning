import os
import img2pdf
from pathlib import Path    
import argparse

#dirname = r"C:\URDU\eBooks\RekhtaDownload\Tuzk-e-Urdu"

def extractPages():
    parser = argparse.ArgumentParser(description='Extract images from PDF document.')
    parser.add_argument('work_dir', help="Output directory for PDF file")
    parser.add_argument('fileName', help='Enter name for New PDF file')    
    parser.add_argument('startPage', help="First page to start extraction")
    parser.add_argument('endPage', help="Last page to start extraction")

    args = parser.parse_args()
    outDir = args.work_dir
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
        
        for fname in os.listdir(outDir):
            if not fname.endswith(".jpg"):
                continue
            pgNum, ext = fname.split('.')
            pageNum = int(pgNum)
            if (pageNum >= pgStart and pageNum <= pgEnd ):
                path = os.path.join(outDir, fname)
                print(path)
                imgs.append(path)
                
                if os.path.isdir(path):
                    continue
        for img in imgs:
            print(img)    
        f.write(img2pdf.convert(imgs))


extractPages()

print('Program Ended')
