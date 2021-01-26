from PyPDF2 import PdfFileReader,PdfFileWriter
#import pathlib
import os
from tkinter import filedialog , Tk
from gooey import Gooey, GooeyParser
from pathlib import Path    


# tkroot = Tk()  # Initializing Tkinter
# outDir = filedialog.askdirectory(parent=tkroot, initialdir="/", title='Please select a directory')


pg_start = 223
pg_end = 231

@Gooey(program_name="Rename Files in Folder")
def extractPages():
    parser = GooeyParser(description='Create Quarterly Marketing Report')
    parser.add_argument('data_directory',
                        action='store',
                        widget='DirChooser',
                        help="Source directory that contains files")
    parser.add_argument('selectFile', action='store',
                        widget='FileChooser', help='Choose your input File')
    parser.add_argument('startPage', help="First page to start extraction")
    parser.add_argument('endPage', help="Last page to start extraction")

    args = parser.parse_args()
    workingDir = args.data_directory
    pdfFullPath = args.selectFile
    pgStart = int(args.startPage)
    pgEnd = int(args.endPage)

    pdf_writer = PdfFileWriter()

    #pdfName = r'مضامین چک بست.pdf'
    pdfName = Path(pdfFullPath).name
    print(pdfName)
    output_filename = f'{pgStart}_{pgEnd}_page_{pdfName}'
    print(output_filename)
    pdf_reader = PdfFileReader(open( os.path.join(workingDir,pdfName), "rb") )

    numofPages = int(pdf_reader.numPages)


    while pgStart <= pgEnd:
        pdf_writer.addPage(pdf_reader.getPage(pgStart-1))
        pgStart += 1

    with open( os.path.join( workingDir,output_filename ), 'wb' ) as out:
        pdf_writer.write(out)

extractPages()
print('Pages extracted')