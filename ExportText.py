import PyPDF2
import os
import json

with open('provided_metadata.json', 'r') as jsonfile:
	metaDict=json.load(jsonfile)


for key in metaDict:
	if "cia" in key:
		fileName=key + '.pdf'
	else:
		fileName="DOC_" + key + ".pdf"
	if os.path.exists(fileName):
		pdfFileObj= open(fileName,'rb')
		pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
		pp=pdfReader.numPages
		docText=""
		for page in range(0,pp):
			pageObj=pdfReader.getPage(page)
			pageText=pageObj.extractText()
			docText=docText+ "------------------\nPage " + str(page) + "\n" + pageText + "\n\n"
		docTextFileName=fileName
		docTextFileName=docTextFileName.split(".")
		docTextFileName=docTextFileName[0]
		docTextFileName=docTextFileName+".txt"
		with open(docTextFileName,'w') as docTextFile:
			docTextFile.write(docText)
		print('Exported: ' + docTextFileName)

	else:
		print(fileName)
