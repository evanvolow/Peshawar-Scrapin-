import json
import os.path

with open('other.json','r') as otherFile:
	otherDict=json.load(otherFile)

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
		for other in otherDict:
			totalOccurrences=0
			termDict=otherDict[other]
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
				#	print(other)
				#	print(term)
				#	print(occurrences)
				totalOccurrences=totalOccurrences+occurrences
			#othercore=float(totalOccurrences)/float(wordcount)*1000000
			if totalOccurrences>0:
				#print(other +str(othercore))
				scoreDict[other]=totalOccurrences
				#print(scoreDict)
		metaDict[ID]["Subjects"]["Other"]=scoreDict
		print(metaDict[ID])

with open('expanded_metadata.json','w') as jsonFile:
	json.dump(metaDict,jsonFile)

