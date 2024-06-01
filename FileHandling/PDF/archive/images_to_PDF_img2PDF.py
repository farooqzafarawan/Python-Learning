import os
import img2pdf
# from tkinter import filedialog , Tk
# from gooey import Gooey, GooeyParser
# from pathlib import Path    


# tkroot = Tk()  # Initializing Tkinter
# outDir = filedialog.askdirectory(parent=tkroot, initialdir="/", title='Please select a directory')

# convert all files ending in .jpg inside a directory
outDir = r"C:\URDU\eBooks\RekhtaDownload"
outFile = os.path.join(outDir, "UmraoJaanAdaa_1_10.pdf")

dirname = r"C:\URDU\eBooks\RekhtaDownload\Umrao Jaan Adaa\umrao-jaan-ada-mirza-hadi-ruswa-ebooks-1"
pg1 = 1
pg2 = 11

with open(outFile,"wb") as f:
	imgs = []
    
	for fname in os.listdir(dirname):
		if not fname.endswith(".jpg"):
			continue
		pgNum, ext = fname.split('.')
		pageNum = int(pgNum)
		if (pageNum >= pg1 and pageNum < pg2 ):
			path = os.path.join(dirname, fname)
			imgs.append(path)
		if os.path.isdir(path):
			continue
		
	f.write(img2pdf.convert(imgs))