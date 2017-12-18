import json
import os.path

with open('people.json','r') as peopleFile:
	peopleDict=json.load(peopleFile)

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
		for person in peopleDict:
			totalOccurrences=0
			termDict=peopleDict[person]
			for key in termDict:
				term=termDict[key]
				occurrences=doctext.count(term)
				#if occurrences > 0:
				#	print("------------------")	
				#	print(filename)
				#	print(person)
				#	print(term)
				#	print(occurrences)
				totalOccurrences=totalOccurrences+occurrences
			#personScore=float(totalOccurrences)/float(wordcount)*1000000
			if totalOccurrences>0:
				#print(person +str(personScore))
				scoreDict[person]=totalOccurrences
				#print(scoreDict)
		metaDict[ID]["Subjects"]={"People":scoreDict}
		print(metaDict[ID])

with open('expanded_metadata.json','w') as jsonFile:
	json.dump(metaDict,jsonFile)

