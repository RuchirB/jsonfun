from datetime import datetime
import os

def timeFormat(timeStamp):
	if(type(timeStamp) is str):
		year = int(timeStamp[0:4])
		month = int(timeStamp[5:7])
		day = int(timeStamp[8:10])
		hour = int(timeStamp[11:13])
		minute = int(timeStamp[14:16])
		sec = int(timeStamp[17:19])
		dateTimeObj = datetime(yearLast, monthLast, dayLast)
		return dateTimeObj
def lastSpokeUpdate(input):
	lastAccessed = open("lastAccessed.txt", "w")
	lastAccessed.write(str(input))
	lastAccessed.close()
	pass
def lastSpoke():
	lastAccessed = open("lastAccessed.txt", "r")
	dateString = lastAccessed.read()
	return datetime.strptime(dateString[0:19], "%Y-%m-%d %H:%M:%S") #reads string from file in teh format of "%Y-%m-%d %H:%M:%S" and puts in datetime object

def constructDatePhrase(date):
	if date.strftime("%y") != 0:
		phrase = date.strftime("%y years, %m months, and %d ago")
	elif date.strftime("%m") != 0:
		phrase = date.strftime("%m months, and %d ago")
	elif date.strftime("%d") != 0:
		phrase = date.strftime("%d days ago")
	elif date.strftime("%H") != 0:
		phrase = date.strftime("%H hours and %M minutes ago")
	elif date.strftime("%M") != 0:
		phrase = date.strftime("%M minutes and %S seconds ago")
	elif date.strftime("%S") != 0:
		phrase = date.strftime("%S seconds ago")
	return phrase

def constructTimeDeltaPhrase(timeDelta):
	hours = str(timeDelta).split(":")[0]
	minutes = str(timeDelta).split(":")[1]
	seconds = str(timeDelta).split(":")[2].split(".")[0]
	
	if int(hours) != 0:
		return(hours + " hours, " + minutes + " minutes " + " and " + seconds + "seconds ago")
	elif int(minutes) != 0:
		return(minutes + " minutes " + "and " + seconds + "seconds ago")
	elif int(minutes) != 0:
		return(seconds + "seconds ago")



#if first time ever interacting with chatbot
if os.path.isfile("lastAccessed.txt") is False:
	lastSpokeUpdate(datetime.utcnow())

timeAgo = datetime.utcnow()-lastSpoke() #constructs a timedelta object

print("Hi, the last time you spoke to me was " +constructTimeDeltaPhrase(timeAgo))
lastSpokeUpdate(datetime.utcnow()) #update the file with the time spoken now for later reference