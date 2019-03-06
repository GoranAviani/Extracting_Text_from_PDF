import PyPDF2

pdfFileObj = open('sample.pdf', 'rb')



pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


print(pdfReader.numPages)


pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

pageObj1 = pdfReader.getPage(1)
print(pageObj1.extractText())




