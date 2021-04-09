from PyPDF2 import PdfFileReader,PdfFileWriter
import argparse
import os
from pathlib import Path    

def extractPages():
    parser = argparse.ArgumentParser(description='Extract images from PDF doc.')
    parser.add_argument('data_directory', help="Directory that contains files")
    parser.add_argument('selectFile', help='Provide input File')
    parser.add_argument('startPage', help="First page to start extraction")
    parser.add_argument('endPage', help="Last page to start extraction")

    args = parser.parse_args()
    workDir = args.data_directory
    pdfFullPath = args.selectFile
    pgStart = int(args.startPage)
    pgEnd = int(args.endPage)

    pdf_writer = PdfFileWriter()

    pdfName = Path(pdfFullPath).name
    print(pdfName)
    output_filename = f'{pgStart}_{pgEnd}_page_{pdfName}'
    print(output_filename)
    pdf_reader = PdfFileReader(open( os.path.join(workDir,pdfName), "rb") )

    numofPages = int(pdf_reader.numPages)

    while pgStart <= pgEnd:
        pdf_writer.addPage(pdf_reader.getPage(pgStart-1))
        pgStart += 1

    with open( os.path.join( workDir,output_filename ), 'wb' ) as out:
        pdf_writer.write(out)

extractPages()
print('Pages extracted')
