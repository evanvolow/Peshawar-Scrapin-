import json
import urllib
import requests
import os.path

with open ('urllist.json', 'r') as file:
	URLDict = json.load(file)
url="https://static.wixstatic.com/media/ce14ca_9d71be60561442719749cbc14f1f3d29.png/v1/fill/w_424,h_397,al_c,usm_0.66_1.00_0.01/ce14ca_9d71be60561442719749cbc14f1f3d29.png"
r = requests.get(url)
with open("test.png", "wb") as testim:
	testim.write(r.content)

for URL in URLDict:
	identifier = URL.replace("/library/readingroom/document/","")
	print("Getting: ",identifier)
	filename = identifier+".pdf"
	if "cia" in filename:
		pass
	else:
		filename="DOC_"+filename
	resourceURL="https://www.cia.gov/library/readingroom/docs/" + filename
	if os.path.exists(filename):
		print("got it")
	else:
		print("gotta get it")
		with open(filename,"wb") as downloading:
			r=requests.get(resourceURL)
			downloading.write(r.content)
		print("Okay now I got it.")
