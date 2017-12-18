import json

with open('people.json','r') as peopleFile:
	peopleDict=json.load(peopleFile)

for key in peopleDict:
	surnameString=peopleDict[key]
	peopleDict[key]={"Surname":surnameString}

print(peopleDict)