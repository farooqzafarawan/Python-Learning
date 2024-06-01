from PyPDF2 import PdfReader,PdfWriter
import os
from pathlib import Path    
#from gooey import Gooey, GooeyParser

# tkroot = Tk()  # Initializing Tkinter
# outDir = filedialog.askdirectory(parent=tkroot, initialdir="/", title='Please select a directory')

pg_start = 223
pg_end = 231

workingDir =  r'C:\TECHNICAL\DATA'
#pdfFullPath = r'C:\TECHNICAL\DATA\SafiaMajid.pdf'

def getPDF_filename():
    # Get Path object of the single PDF file in workingDir
    pdf_file_path = next(Path(workingDir).glob('*.pdf'), None)

    if pdf_file_path is not None and pdf_file_path.is_file():
        # Get full filename
        full_filename = pdf_file_path.name

        # Get filename without extension
        filename_without_extension = pdf_file_path.stem

        return pdf_file_path
        # print("Full filename of PDF file:", full_filename)
        # print("Filename without extension of PDF file:", filename_without_extension)
    else:
        print("No PDF file found in the specified directory.")

def extractPages():
    pgStart = 1
    pgEnd = 3

    
    pdfFullPath = getPDF_filename()
    pdfName = pdfFullPath.stem
    #pdfName = r'SafiaMajid.pdf'
    #pdfName = Path(pdfFullPath).name
    #print(pdfName)
    
    pdf_reader = PdfReader(open( os.path.join(workingDir,pdfFullPath), "rb") )

    
    numofPages = len(pdf_reader.pages)

    for page in range(1, numofPages):
        output_filename = f'{pdfName}_pg{page}.pdf'
        writePDF(workingDir, pdf_reader, page, output_filename)


    # while pgStart <= pgEnd:
    #     output_filename = f'{pdfName}_pg{pgStart}.pdf'
    #     writePDF(workingDir, pdf_reader, pgStart-1, output_filename)
    #     pgStart += 1    


def writePDF(workingDir, reader, pageNum, output_filename):
    # changed addPage and reader.getPages(pgStart-1) 
    pdf_writer = PdfWriter()
    pdf_writer.add_page(reader.pages[pageNum])

    with open( os.path.join( workingDir,output_filename ), 'wb' ) as out:
        pdf_writer.write(out)

extractPages()
print('Pages extracted')