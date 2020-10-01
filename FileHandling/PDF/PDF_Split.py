from PyPDF2 import PdfFileReader

def split_pdf_to_two(filename,pg_num,numSplits):
    pdf_reader = PdfFileReader(open(filename, "rb"))
    try:

        filePDF = pathlib.Path(PDFfile)
        PDF_Name, PDF_ext = filePDF.stem, filePDF.suffix    
        
        pg_start = "0"
        pg_end = int(pdf_reader.numPages/numSplits)
        
        for i in range(numSplits):
            outPDF = PDF_Name + '_' + pg_start + '_' + str(pg_end) + PDF_ext
            outPDF = os.path.join(outDir,outPDF)
            print(outPDF)

            if i == (numSplits-2):
                pg_start = str(pg_end+1)
                pg_end = pdf_reader.numPages
            else:
                pg_start = str(pg_end+1)
                pg_end = pg_end+pg_end


        
        assert pg_num < pdf_reader.numPages
        print(pdf_reader.numPages)

    except AssertionError as e:
        print("Error: The PDF you are cutting has less pages than you want to cut!")

PDFfile = r'C:\AWS\AWS_Solutions.pdf'
pageNum = 250

split_pdf_to_two(PDFfile, pageNum,3)
