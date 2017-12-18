import csv
import json

with open('expanded_metadata.json','r') as jsonfile:
	metaDict=json.load(jsonfile)

with open('expanded_metadata.csv','w') as csvfile:
	writer=csv.writer(csvfile)
	count=0
	for ID in metaDict:
		itemDict=metaDict[ID]
		linkText="https://www.cia.gov/library/readingroom/document/" + ID
		if "Title" in itemDict:
			title=itemDict["Title"]
			print(title)
		else:
			title="untitled"
			print("Missing title: " + ID)
		relEst=itemDict["Relevance Estimate"]
		if "Publication Date" in itemDict:
			originalDate=itemDict["Publication Date"]
		else:
			originalDate="undated"
			print("Missing date: " + ID)
		if "Document Page Count" in itemDict:
			pageCount=itemDict["Document Page Count"]
		else:
			pageCount=""
		if "Subjects" in itemDict:
			subjectDict=itemDict["Subjects"]
			
			peopleDict=subjectDict["People"]
			peopleString=""
			for key in peopleDict:
				peopleString=peopleString + key + " (" + str(peopleDict[key]) + "); "
			
			orgDict=subjectDict["Organizations"]
			orgString=""
			for key in orgDict:
				orgString=orgString + key + " (" + str(orgDict[key]) + "); "
			
			geoDict=subjectDict["Geography"]
			geoString=""
			for key in geoDict:
				geoString=geoString + key + " (" + str(geoDict[key]) + "); "

			otherDict=subjectDict["Other"]
			otherString=""
			for key in otherDict:
				otherString=otherString + key + " (" + str(otherDict[key]) + "); "
		else:
			peopleString=""
			orgString=""
			geoString=""
			otherString=""

		row=[ID,relEst,title,originalDate,pageCount,peopleString,orgString,geoString,otherString,linkText]
		writer.writerow(row)
		count=count+1
		print(count)