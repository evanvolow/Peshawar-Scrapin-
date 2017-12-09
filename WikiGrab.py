import re
import requests
from bs4 import BeautifulSoup

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

terms={'people':[], "orgs":[], "other":[]}


for link in linkList:
	linkText=link.replace("[[","")
	linkText=linkText.replace("]]","")
	print("------------------")
	inputYN=input("Add " + linkText + " to terms? y/n---> ")
	if inputYN is "y":
		print("Is " + linkText + " a person or organization?")
		category=input("Type p for person or o for org. Otherwise just press enter---> ")
		if category is "p":
			if "|" in linkText:
				linkText=linkText.split("|")
			else:
				nameSplit=linkText.split(" ")
				surname=nameSplit[len(nameSplit)-1]
				linkText=[linkText, surname]
			terms['people'].append(linkText)
		if category is "o":
			terms['orgs'].append(linkText)
		else:
			terms['other'].append(linkText)
	elif inputYN is "n":
		print("aw nah")
	elif inputYN is "quit":
		break
	else:
		break

print(terms)

print("Donezo")