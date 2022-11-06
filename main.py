from os import system as cmd
from os import listdir as files
from random import randint as random
message = ""
read = open("path.txt", "r")
messagefile = open("messages.txt", "r")
messages = messagefile.readlines()
for i in range(random(0, len(messages))):
	message = messages[i]
lines = read.readlines()
path = lines[1]
cmd("cd " + path)
cmd("git remote add origin " + lines[0])
cmd("git add .")
cmd("git push --set-upstream origin master")
cmd("git commit -m " + "\"" + message + "\"")
read.close()
write = open("path.txt", "w")
write.write("")
write.close()
messagefile.close((
clear = open("path.txt", "w")
clear.write("")
clear.close()
cmd("git remote remove origin")
print("Finished")
