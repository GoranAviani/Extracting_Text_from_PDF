import PyPDF2

pdfFileObj = open('sample.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#printing total page numebers of an pdf
print(pdfReader.numPages)

#reading page 1
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

#reading page 2
pageObj1 = pdfReader.getPage(1)
print(pageObj1.extractText())




