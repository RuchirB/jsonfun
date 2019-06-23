import requests, datetime

#listOfThree = list()
class Helper:
	#listOfThree contains the three latest news story names
	listOfThree = []
	jsonRequest = []

	@staticmethod
	def init():
		resp = requests.get('https://newslens.berkeley.edu/api/lanes/recent2')
		Helper.jsonRequest = resp.json()
		#Grab top three stories in a list
		for x in range(3):
			Helper.listOfThree.append(Helper.jsonRequest[x]["story_name"])

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


		print("The " +storyName + " story started " +(str(daysAgo)) + " hours ago." +" The latest update from this story comes from " +(str(daysAgoLast)) +" hours ago, when " + storySummary)
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


storyIndex = 0

Helper.init()
print("Hi, I'm NewsLens!")
userInput = input()

if("new" in userInput):
	Helper.displayNewsStories()

userInput = input()
#if userInput contains something from listOfThree, get that index and call a method elaborate that further describes it
for x in Helper.listOfThree:
	breakLoop=False
	for individualWord in userInput.split():
		if individualWord.lower() in x.lower():
			#print("Found it in " +x +" print " +str(Helper.listOfThree.index(x)))
			storyIndex=Helper.listOfThree.index(x)
			Helper.elaborateOnStory(storyIndex)
			breakLoop=True
			break
	if breakLoop is True:
		break

userInput = input()

if("last" in userInput or "10 events" in userInput):
	Helper.last10Events(storyIndex)
elif("people" in userInput or "said" in userInput):
	Helper.peopleSaid(storyIndex)

userInput = input()

if("last" in userInput or "10 events" in userInput):
	Helper.last10Events(storyIndex)
elif("people" in userInput or "said" in userInput):
	Helper.peopleSaid(storyIndex)
