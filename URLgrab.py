import requests, re
from bs4 import BeautifulSoup
import json

titleDict={}

for pagenum in range(0,364):
	print("Scrapin' page ", pagenum)	
	searchURL="https://www.cia.gov/library/readingroom/advanced-search-view?keyword=afghanistan&ds_field_pub_date_op=between&ds_field_pub_date[min]=1979&ds_field_pub_date[max]=1989&page=" + str(pagenum)
	searchResultsPage=requests.get(searchURL, verify=False)
	searchResultsText=searchResultsPage.text
	soup=BeautifulSoup(searchResultsText,"html.parser")

	resultTable=soup.find("tbody")
	titles=resultTable.find_all("a", text=True)


	for key in titles:
		dictKey=key.text
		dictURL=key['href']
		titleDict[dictURL]=dictKey

with open('urllist.json', 'w') as jsonfile:
	json.dump(titleDict, jsonfile)

print(titleDict)