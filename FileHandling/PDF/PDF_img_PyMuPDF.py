# pip install PyMuPDF
import fitz  # PyMuPDF
from pathlib import Path

BASE_DIR = r'C:\URDU\eBooks\PDF books\MISC'
fileName = 'Laal Qilay ky Shaam-e-Sahar'
ext = '.pdf'


def get_pixmaps_in_pdf(pdf_filename):
    doc = fitz.open(pdf_filename)
    xrefs = set()
    for page_index in range(doc.pageCount):
        for image in doc.getPageImageList(page_index):
            xrefs.add(image[0])  # Add XREFs to set so duplicates are ignored
    pixmaps = [fitz.Pixmap(doc, xref) for xref in xrefs]
    doc.close()
    return pixmaps


def write_pixmaps_to_pngs(pixmaps):

    for i, pixmap in enumerate(pixmaps):
        pixmap.writePNG(f'{path}{i}.png')


path = Path(BASE_DIR)/fileName

pixmaps = get_pixmaps_in_pdf(str(path)+ext)
write_pixmaps_to_pngs(pixmaps)
