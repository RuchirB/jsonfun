import urllib.request, json

#Grabs JSON file from URL
jsonUrl = urllib.request.urlopen("https://newslens.berkeley.edu/api/lanes/recent2")

print(type(jsonUrl))
#Referencing index 0 since newLensAPI.json is actuallhy a list of one index that contains the json object
jsonDictionary = json.load(jsonUrl)[0]


#WThis returns a list unless you add "[0]" to the above line. then it returns a dict
print(type(jsonDictionary))

with open ("/Users/ruchirbaronia/Desktop/PythonProjects/JSONfun/newsLensAPI.json", "w") as jsonFile:
	json.dump(jsonDictionary, jsonFile, indent=3)


#All the high level categories
for subDict in jsonDictionary:
	print(subDict)


print("_____________________________________TOP HIGHLIGHTS_____________________________________________________")

for newsHighlights in jsonDictionary["latest_highlights"]:
	print(newsHighlights["title"])
