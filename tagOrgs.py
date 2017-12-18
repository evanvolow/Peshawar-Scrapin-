import json
import os.path

with open('orgs.json','r') as orgsFile:
	orgsDict=json.load(orgsFile)

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
		for org in orgsDict:
			totalOccurrences=0
			termDict=orgsDict[org]
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
				#	print(org)
				#	print(term)
				#	print(occurrences)
				totalOccurrences=totalOccurrences+occurrences
			#orgScore=float(totalOccurrences)/float(wordcount)*1000000
			if totalOccurrences>0:
				#print(org +str(orgScore))
				scoreDict[org]=totalOccurrences
				#print(scoreDict)
		metaDict[ID]["Subjects"]["Organizations"]=scoreDict
		print(metaDict[ID])

with open('expanded_metadata.json','w') as jsonFile:
	json.dump(metaDict,jsonFile)

