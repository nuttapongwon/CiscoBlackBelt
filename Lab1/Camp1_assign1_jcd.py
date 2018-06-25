import json
file = open("SessionsAttended.json", "r") 
data = json.load(file)
attendedSession = data["sessions"]
data_sessions = attendedSession.split(',')

n = len(data_sessions)

print ("I have attended " + str(n) + " sessions!!")