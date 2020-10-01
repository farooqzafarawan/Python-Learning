import os
import img2pdf

# convert all files ending in .jpg inside a directory
outDir = r"C:\URDU\eBooks\RekhtaDownload"
outFile = os.path.join(outDir, "Tuzk-e-Urdu.pdf")

dirname = r"C:\URDU\eBooks\RekhtaDownload\Tuzk-e-Urdu"

with open(outFile,"wb") as f:
	imgs = []
    
	for fname in os.listdir(dirname):
		if not fname.endswith(".jpg"):
			continue
		path = os.path.join(dirname, fname)
		if os.path.isdir(path):
			continue
		imgs.append(path)
	f.write(img2pdf.convert(imgs))