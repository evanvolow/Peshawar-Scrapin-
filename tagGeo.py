import json
import os.path

with open('geoterms2.json','r') as geoFile:
	geoDict=json.load(geoFile)

with open('expanded_metadata.json','r') as metaFile:
	metaDict=json.load(metaFile)
zerolist=[]
for ID in metaDict:
	if "cia" in ID:
		filename = ID + ".txt"
	else:
		filename="DOC_" + ID + ".txt"
	if os.path.exists(filename):
		with open(filename,'r') as document:
			doctext=document.read()
			tempwords=doctext.split(None)
			wordcount=len(tempwords)

		scoreDict={}
		for geo in geoDict:
			totalOccurrences=0
			termDict=geoDict[geo]
			for key in termDict:
				term=termDict[key]
				occurrences=doctext.count(term+" ")
				occurrences=occurrences+doctext.count(term+".")
				occurrences=occurrences+doctext.count(term+",")
				occurrences=occurrences+doctext.count(term+":")
				occurrences=occurrences+doctext.count(term+";")
				occurrences=occurrences+doctext.count(term+"-")
				#if occurrences > 0:
				#	print("------------------")	
				#	print(filename)
				#	print(geo)
				#	print(term)
				#	print(occurrences)
				totalOccurrences=totalOccurrences+occurrences
			#geocore=float(totalOccurrences)/float(wordcount)*1000000
			if totalOccurrences>0:
				if "primaryName" in termDict:
					useName=termDict["primaryName"]
				else:
					useName=term
				scoreDict[useName]=totalOccurrences
				#print(scoreDict)
		metaDict[ID]["Subjects"]["Geography"]=scoreDict
		print(metaDict[ID])

with open('expanded_metadata.json','w') as jsonFile:
	json.dump(metaDict,jsonFile)

