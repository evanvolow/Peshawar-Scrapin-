import json
import os

with open("expanded_metadata.json","r") as metaFile:
	metaDict=json.load(metaFile)

with open("relevence.json","r") as relTermsFile:
	relDict=json.load(relTermsFile)
for ID in metaDict:
	if "cia" in ID:
		filename = ID + ".txt"
	else:
		filename="DOC_" + ID + ".txt"
	if os.path.exists(filename):
		print(filename)
		totalOccurrences=0
		with open(filename,'r') as document:
			doctext=document.read()
		tempwords=doctext.split(None)
		wordcount=len(tempwords)
		print(wordcount)
		counted=[]
		points=0
		
		itemMetadata=metaDict[ID]
		subjectDict=itemMetadata["Subjects"]
		
		geoDict=subjectDict["Geography"]
		for key in geoDict:
			points=points+geoDict[key]

		peopleDict=subjectDict["People"]
		for key in peopleDict:
			if key in relDict:
				points=points+peopleDict[key]

		orgDict=subjectDict["Organizations"]
		for key in orgDict:
			if key in relDict:
				points=points+orgDict[key]

		otherDict=subjectDict["Other"]
		for key in otherDict:
			if key in relDict:
				points=points+otherDict[key]
		
		relIndex=float(points)/float(wordcount)*10000
		relIndex=int(relIndex)
		if relIndex>100:
			relIndex=100
		metaDict[ID]["Relevence Estimate"]=relIndex

		print(metaDict[ID]['Title'])
		print(relIndex)
		print("------------------")
with open('expanded_metadata.json','w') as jsonFile:
	json.dump(metaDict,jsonFile)