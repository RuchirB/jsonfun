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
		storyTime = Helper.jsonRequest[storyIndex]["latest_highlights"][storyIndex]["pubtime"]
		year = int(storyTime[0:4])
		month = int(storyTime[5:7])
		day = int(storyTime[8:10])
		print(str(year) + str(month) + str(day))
		date = datetime.datetime(year, month, day)
		daysAgo = datetime.datetime.utcnow() - date
		storySummary = Helper.jsonRequest[storyIndex]["latest_highlights"][storyIndex]["summary"]
		storyName = Helper.jsonRequest[storyIndex]["story_name"]
		print("The " +storyName + " story started " +(str(daysAgo)) + " hours ago, when " + storySummary +".")



Helper.init()
print("Hi, I'm NewsLens!")
userInput = input()

if("new" in userInput):
	Helper.displayNewsStories()

userInput = input()
#if userInput contains something from listOfThree, get that index and call a method elaborate that further describes it
breakLooop = False
for x in Helper.listOfThree:
	for individualWord in userInput.split():
		print("checking for " +individualWord + " in " + x)
		if individualWord.lower() in x.lower():
			#print("Found it in " +x +" print " +str(Helper.listOfThree.index(x)))
			Helper.elaborateOnStory(Helper.listOfThree.index(x))
			breakLoop=True
			break
	if breakLoop is True:
		break
