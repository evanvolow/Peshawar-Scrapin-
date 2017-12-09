import json
import urllib
import requests, re
import unicodedata
from bs4 import BeautifulSoup

with open ('urllist.json', 'r') as file:
	URLDict = json.load(file)

masterDict={}
progressCounter=0

for URL in URLDict:
	identifier = URL.replace("/library/readingroom/document/","")
	progressCounter=progressCounter+1
	print("Getting: ",identifier)
	print("Document number" + str(progressCounter))
	filename = identifier+".pdf"
	resourceURL="https://www.cia.gov/library/readingroom/document/" + identifier
	r=requests.get(resourceURL)
	parsable=r.text
	soup=BeautifulSoup(parsable, "html.parser")

	dataBlock=soup.find("div", attrs={"class":"content clearfix"})
	metaDict={}
	titleString=soup.find("h1", attrs={'class':'documentFirstHeading'}).text
	metaDict['Title']=titleString
	fieldsList=dataBlock.findAll("div", attrs={"class":"field-label"})
	contentList=dataBlock.findAll("div", attrs={"class":"field-item even"})
	for item in fieldsList:
		index=fieldsList.index(item)
		fieldName=item.text
		if "Body" not in fieldName and "File" not in fieldName:
			fieldName=fieldName.replace("\xa0", "")
			fieldName=fieldName.replace(":","")
			fieldName=fieldName.strip()
			if "Date" in fieldName:
				contentHTML=contentList[index]
				standardDateForm=re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')
				match=re.search(standardDateForm, str(contentHTML))
				if match is None:
					fieldContent=""
				else:
					standardDate=(match.group())
					fieldContent=standardDate
			else:	
				fieldContent=contentList[index].text
			metaDict[fieldName]=fieldContent
		else:
			pass

	masterDict[identifier]=metaDict


with open ('provided_metadata.json','w') as output:
	json.dump(masterDict, output)

#print(masterDict)

