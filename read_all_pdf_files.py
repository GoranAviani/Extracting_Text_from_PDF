import PyPDF2, os

pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)


pdfFiles.sort(key= str.lower)


#from reading_pdf.py:
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    print("\n here comes: ")
    print(pageObj.extractText())