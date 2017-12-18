import csv
import json

geoDict={}

with open('geo_compact3.csv',newline='', encoding='utf-8') as csvFile:
	reader=csv.reader(csvFile)
	for row in reader:
		UFI = str(row[0])
		UNI = str(row[1])
		name = row[2]
		rank=row[3]
		dictKey="UFI"+UFI
		subDictKey="UNI"+UNI
		if dictKey not in geoDict:
			subDict={}
			if row[3] is "1":
				print('yeth')
				subDict["primaryName"]=name
			else:
				subDict[subDictKey]=name
		else:
			subDict=geoDict[dictKey]
			print(subDict)
			if row[3] is "1":
				subDict["primaryName"]=name
				print('yethagain')
			else:
				subDict[subDictKey]=name
		geoDict[dictKey]=subDict

print(geoDict)

with open('geoterms2.json','w') as jsonfile:
	json.dump(geoDict, jsonfile)