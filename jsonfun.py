import json
#Converting JSON file to a dictioanry object
with open('/Users/ruchirbaronia/Desktop/JSONfun/philippe_messages.json') as philippesMessage:
	data = json.load(philippesMessage) 

#Printing the three messages individually
print (data["message1"]) 
print (data["message2"])
print (data["message3"]) 

#Converting back into a JSON file called dataFile.json
with open ("dataFile.json", "w") as philippesOutput:
	json.dump(data, philippesOutput, indent=3)

#Converting into a string and reprinting with each child indented 3 spaces
print(json.dumps(data, indent=3))
for myString in data:
	if(data[myString].startswith("I")):
		print (myString + " starts with an I")
