import requests

class Helper:
	#listOfThree contains the three latest news story names
	listOfThree = ["a", "b", "c"]

	@staticmethod
	def init():
		jsonRequest = requests.get('https://newslens.berkeley.edu/api/lanes/recent2')
		#Grab top three stories in a list
		for x in range(3):
			listOfThree[x] = jsonRequest[x]["story_name"]

	@staticmethod
	def displayNewsStories():
		print(listOfThree[0])
		#print("Hello! Today's important news stories are " +listOfThree[0] + ", " + listOfThree[1] + ", and" +listOfThree[2] ". (There's also been an update in W that we talked about last week.")


Helper.init()
print("Hi, I'm NewsLens!")
userInput = input()

if("new" in userInput):
	Helper.displayNewsStories()

