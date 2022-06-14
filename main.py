from os import system as cmd
from os import listdir as files
from random import randint as random
message = ""
read = open("path.txt", "r")
messages = open("messages.txt", "r").readlines()
for i in range(random(0, len(messages))):
	message = messages[i]
lines = read.readlines()
path = lines[1]
cmd("cd " + path)
cmd("git remote add origin " + lines[0])
cmd("git add .")
cmd("git commit -m " + "\"" + message + "\"")
write = open("path.txt", "w")
write.write("")
read.close()
write.close()
cmd("git remote remove origin")
print("Finished")
