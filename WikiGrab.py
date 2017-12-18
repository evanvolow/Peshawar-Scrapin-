import re
import requests
from bs4 import BeautifulSoup
import json


#with open('terms.json','r') as termFile:
#	terms=json.load(termFile)

inputURL=input("Enter Wikipedia URL")

r=requests.get(inputURL, verify=False)
inputHTML=r.text
soup=BeautifulSoup(inputHTML,"html.parser")
title=soup.find("title").text
title=title.replace(" ","_")
title=title.replace("_-_Wikipedia","")
print(title)


editURL="https://en.wikipedia.org/w/index.php?title=" + title + "&action=edit"
r=requests.get(editURL, verify=False)
editHTML=r.text
soup=BeautifulSoup(editHTML, "html.parser")
editBox=str(soup.find("textarea"))
editBox=editBox.replace("]]",']]\n')

links=re.compile('\[\[.*\]\]')
linkList=links.findall(editBox)


print(linkList)

with open('people.json','r') as loadPeople:
	people=json.load(loadPeople)
with open('orgs.json','r') as loadOrgs:
	orgs=json.load(loadOrgs)
with open('other.json','r') as loadOther:
	other=json.load(loadOther)
with open('relevence.json','r') as loadRel:
	relevence=json.load(loadRel)
with open('checked.json','r') as loadCheck:
	checked=json.load(loadCheck)

#oldPeople={}
#oldOrgs={}
#oldOther={}


def cleanLink(rawLink):
	rawLink=rawLink.replace("[[","")
	rawLink=rawLink.replace("]]","")
	rawLink=rawLink.split("(")
	rawLink=rawLink[0]
	rawLink=rawLink.strip()
	rawLink=rawLink.split('|')
	rawLink=rawLink[0]
	return(rawLink)


for link in linkList:
	linkText=cleanLink(link)
	if linkText in str(checked):
		pass
	elif linkText in people:
		pass
	elif linkText in orgs:
		pass
	elif linkText in other:
		pass
	else:
		checked[linkText]=link
		print("------------------")
		inputYN=input("Add " + linkText + " to terms? y/n---> ")
		if inputYN is "y":
			print("Is " + linkText + " a person or organization?")
			category=input("Type p for person or o for org. Otherwise just press enter---> ")
			if category is "p":
				nameSplit=linkText.split(" ")
				surname=nameSplit[len(nameSplit)-1]
				people[linkText]={"surname":surname}
				relEntry={"surname":surname}
			if category is "o":
				orgs[linkText]={"primaryname":linkText}
				relEntry={"primaryname":linkText}
			else:
				other[linkText]={"primaryname":linkText}
				relEntry={"primaryname":linkText}
			relevent=input('Add to relevence testing terms? y/n---> ')
			if relevent is "y":
				relevence[linkText]=relEntry
		elif inputYN is "n":
			pass
		elif inputYN is "quit":
			break
		else:
			break


with open('people.json','w') as peopleFile:
	json.dump(people, peopleFile)
with open('orgs.json','w') as orgsFile:
	json.dump(orgs, orgsFile)
with open('other.json','w') as otherFile:
	json.dump(other, otherFile)
with open('relevence.json','w') as relFile:
	json.dump(relevence, relFile)
with open('checked.json','w') as checkedFile:
	json.dump(checked,checkedFile)


print("Donezo")