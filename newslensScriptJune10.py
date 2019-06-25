import requests, datetime, dateTimeModule, json

#listOfThree = list()
class Helper:
	#listOfThree contains the three latest news story names
	listOfThree = []
	jsonRequest = []
	listOfHistory = []

	@staticmethod
	def init():
		resp = requests.get('https://newslens.berkeley.edu/api/lanes/recent2')
		Helper.jsonRequest = resp.json()
		#Grab top three stories in a list
		for x in range(3):
			Helper.listOfThree.append(Helper.jsonRequest[x]["story_name"])
		Helper.loadSavedHistory()

	@staticmethod
	def displayNewsStories():
		print("Hello! Today's important news stories are " +Helper.listOfThree[0] + ", " + Helper.listOfThree[1] + ", and " +Helper.listOfThree[2] +". (There's also been an update in W that we talked about last week.")

	@staticmethod
	def elaborateOnStory(storyIndex):
		#information needed: Date of story & summary of first event
		storyTime = Helper.jsonRequest[storyIndex]["extent"]["start"]
		year = int(storyTime[0:4])
		month = int(storyTime[5:7])
		day = int(storyTime[8:10])
		date = datetime.datetime(year, month, day)
		#story started @
		daysAgo = datetime.datetime.utcnow() - date
		storySummary = Helper.jsonRequest[storyIndex]["latest_highlights"][0]["summary"]

		#story name
		storyName = Helper.jsonRequest[storyIndex]["story_name"]

		#Last Update
		storyTimeLast = Helper.jsonRequest[storyIndex]["latest_highlights"][0]["pubtime"]
		yearLast = int(storyTimeLast[0:4])
		monthLast = int(storyTimeLast[5:7])
		dayLast = int(storyTimeLast[8:10])
		dateLast = datetime.datetime(yearLast, monthLast, dayLast)
		#story started @
		daysAgoLast = datetime.datetime.utcnow() - dateLast

		#Saving story
		Helper.saveStoryName(Helper.jsonRequest[storyIndex]["id"])

		print("The " +storyName + " story started " +dateTimeModule.constructTimeDeltaPhrase(daysAgo) +" The latest update from this story comes from " +dateTimeModule.constructTimeDeltaPhrase(daysAgoLast) +" when " + storySummary)
		print("\n Do you want me to tell you what people have said or walk you through the last 10 events in the story?")

	@staticmethod
	def last10Events(storyIndex):
		print("_____________Here are the last ten events: _________________")
		storyEvents = Helper.jsonRequest[storyIndex]["latest_highlights"]
		for x in range (10):
			print(str(x+1) +") "+storyEvents[x]["summary_title"] + "\n")

	@staticmethod
	def peopleSaid(storyIndex):
		highlightInfoUrl = "https://newslens.berkeley.edu/api/highlight_info/" + str(Helper.jsonRequest[storyIndex]["latest_highlights"][0]["_id"] )
		peopleInfoUrl = "https://newslens.berkeley.edu/api/story/" + str(Helper.jsonRequest[storyIndex]["latest_highlights"][0]["ntopic"])+ "/people"
		highlightJson = requests.get(highlightInfoUrl).json()
		peopleList = requests.get(peopleInfoUrl).json()

		#print(peopleList)
		print(peopleList[0]["name"] +", " +peopleList[1]["name"] + ", and " +peopleList[2]["name"] +" commented on the issue. " + peopleList[2]["name"] 
			+" said \"" + highlightJson["descriptions"][2]["para"] +"\"")

	@staticmethod
	def loadSavedHistory():
		storyFile = open("/Users/ruchirbaronia/Desktop/PythonProjects/JSONfun/storyInteractions.txt", "a+")
		Helper.listOfHistory = storyFile.readlines()

	@staticmethod
	def saveStoryName(storyId):

		for y in range(len(Helper.jsonRequest)):
			if Helper.jsonRequest[y]["id"] == int(storyId):
				storyName= Helper.jsonRequest[y]["story_name"]
		
		myDict = {"story_name":storyName, "id":storyId, "accessTime":str(datetime.datetime.utcnow())}
		Helper.listOfHistory.append(myDict)

		storyFile = open("/Users/ruchirbaronia/Desktop/PythonProjects/JSONfun/storyInteractions.txt", "a+")
		
		for jsonFile in Helper.listOfHistory:
			storyFile.write("%s\n" %jsonFile)


		#json.dump(myDict, storyFile, indent=1)
		storyFile.close()



storyIndex = 0

def elaborateOnStory(userInput):
	#if userInput contains something from listOfThree, get that index and call a method elaborate that further describes it
	print("elaborating on " +userInput)
	elaborated = False
	for x in Helper.listOfThree:
		breakLoop=False
		for individualWord in userInput.split():
			if individualWord.lower() in x.lower():
				#print("Found it in " +x +" print " +str(Helper.listOfThree.index(x)))
				storyIndex=Helper.listOfThree.index(x)
				Helper.elaborateOnStory(storyIndex)
				elaborated = True
				breakLoop=True
				break
		if breakLoop is True:
			break
	return elaborated

def lastTenEventsOrPeople(userInput):
	if("last" in userInput or "10 events" in userInput):
		Helper.last10Events(storyIndex)
		return True
	elif("people" in userInput or "said" in userInput):
		Helper.peopleSaid(storyIndex)	
		return True
	else:
		return False


def giveUserHistory():
	storyFile = open("/Users/ruchirbaronia/Desktop/PythonProjects/JSONfun/storyInteractions.txt", "r")
	array = storyFile.readlines()
	print("Here are the stories you've asked about before: \n")
	for x in array: #for every line in the history file
		dictionary = json.loads(x)
		id = dictionary["id"] #Pull out the ID from the line
		print("USER ID " +id)
		print(dictionary["story_name"])
	storyFile.close()

def getUpdatesOn(storyInput):
	print("Would you like updates on any of these stories?")
	answer  = False
	while answer != True:
		userInput = input()
		if "yes" in userInput:
			print("Which story would you like updates on?")
			getUpdatesOn(input())
			answer = True
		elif "no" in userInput:
			print("Okay, sure! For a list of things you can ask, type help.")
			answer= True
		else:
			print("What?")

	

#TODO:
#Test that this code displays all the user history properly.
#Create method that gets all updates for a certain story after a certain date. Parameters (Story_name, date_accessed). Then use this same function to allow the user to ask for give me updates on the XXX story from YYY date. search XXX in ALL storynames & pull updates from YYY
#Allow user to ask for a specific person name, search for it in database and pull info about it
#After implementing the above, store any specific people names in a separate history file with date accessed
#implement the help command 

Helper.init()
print("Hi, I'm NewsLens!")
while(exit != True):
	alreadyResponded = False
	userInput = input() #Hi newslens whats new

	if(alreadyResponded != True and "exit" in userInput):
		exit=True
		dateTimeModule.lastSpokeUpdate(datetime.datetime.utcnow()) #update the file with the time spoken now for later reference
	if("new" in userInput):
		Helper.displayNewsStories()
		alreadyResponded = True

	if alreadyResponded != True:
		alreadyResponded = elaborateOnStory(userInput)

	if alreadyResponded != True:
		alreadyResponded = lastTenEventsOrPeople(userInput)

	if alreadyResponded != True and "history" in userInput:
		alreadyResponded = giveUserHistory()

	#if alreadyResponded != True 
	
