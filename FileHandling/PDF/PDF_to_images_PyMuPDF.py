import fitz  # PyMuPDF
from PIL import Image
from pathlib import Path

def pdf_to_images(pdf_dir, output_folder):
    pdf_dir = Path(pdf_dir)
    output_folder = Path(output_folder)

    # Find the only PDF file in the directory using a single line
    pdf_path = next(pdf_dir.glob("*.pdf"), None)

    #  Find the only PDF file in the directory using a single line
    # pdf_files = list(pdf_dir.glob("*.pdf"))
    # pdf_path = pdf_files[0]

    # Open the PDF file
    pdf_doc = fitz.open(pdf_path)

    # Ensure the output folder exists
    output_folder.mkdir(parents=True, exist_ok=True)

    for pageNum in range(len(pdf_doc)):
        # Get the page
        page = pdf_doc.load_page(pageNum)

        # Get the page dimensions
        pix = page.get_pixmap()

        # Create an image object from the pixmap
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image
        image_path = output_folder / f"page_{pageNum + 1}.png"
        image.save(image_path)
        print(f"Saved: {image_path}")

# Working Directory and Output Folder
workingDir = Path("C:/TECHNICAL/DATA")
outputFolder = Path("C:/TECHNICAL/DATA/output")
pdf_to_images(workingDir, outputFolder)

