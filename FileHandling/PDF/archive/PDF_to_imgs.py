from PyPDF4 import PdfFileReader,PdfFileWriter
from os.path import join
import argparse
from PIL import Image
import io

workDir = r'C:\URDU\eBooks\PDF books\MISC'
#fileName = 'Laal Qilay ky Shaam-e-Sahar'
fileName = 'Siraab Maghrib'
a = 'سراب مغرب'
ext = '.pdf'

jpg = '.jpg'
jp2 = '.jp2'
png = '.png'
tiff = '.tiff'


def extractImages():
    # parser = argparse.ArgumentParser(prog='PDFtoImage',description='Extracting images from PDF')
    # parser.add_argument('infile', help='Enter name for input source PDF file')
    # args = parser.parse_args()
    # fileName= args.infile

    filePDF = join(workDir, fileName+ext)

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
                    img = Image.open(io.BytesIO(data))
                    outFile = join(workDir, f'{pgNum}_{fileName}{jpg}')
                    img.save(outFile)
                    # img = open(join(workDir, f'{pgNum} {fileName}{jpg}'), "wb")
                    # img.write(data)
                    # img.close()
                elif xObject[obj]['/Filter'] == '/JPXDecode':
                    img = open(join(workDir, f'{pgNum} {fileName}{jp2}'), "wb")
                    img.write(data)
                    img.close()
                elif xObject[obj]['/Filter'] == '/CCITTFaxDecode':
                    img = open(join(workDir, f'{pgNum} {fileName}{tiff}'), "wb")
                    img.write(data)
                    img.close()


if __name__ == '__main__':
    extractImages()

print('Pages extracted')
