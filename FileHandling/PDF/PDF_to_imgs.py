from PyPDF4 import PdfFileReader,PdfFileWriter
from os.path import join
#import PyPDF2
from PIL import Image

workDir = r'C:\URDU\eBooks\PDF books\MISC'
fileName,ext = 'Laal Qilay ky Shaam-e-Sahar', '.pdf'
filePDF = join(workDir, fileName+ext)

jpg = '.jpg'
jp2 = '.jp2'
png = '.png'

def extractImages():
    pdfReader = PdfFileReader(open(filePDF, "rb"))

    for pgNum in range(pdfReader.numPages):
        page = pdfReader.getPage(pgNum)
        xObject = page['/Resources']['/XObject'].getObject()

        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                data = xObject[obj].getData()
                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                    mode = "RGB"
                else:
                    mode = "P"

                if xObject[obj]['/Filter'] == '/FlateDecode':
                    img = Image.frombytes(mode, size, data)
                    outFile = join(workDir, f'{pgNum}_{fileName}{png}')
                    img.save(outFile)
                elif xObject[obj]['/Filter'] == '/DCTDecode':
                    img = open(join(workDir, f'{pgNum} {fileName}{jpg}'), "wb")
                    img.write(data)
                    img.close()
                elif xObject[obj]['/Filter'] == '/JPXDecode':
                    img = open(join(workDir, f'{pgNum} {fileName}{jp2}'), "wb")
                    img.write(data)
                    img.close()


if __name__ == '__main__':
    extractImages()

print('Pages extracted')
