from os import system as cmd
from os import listdir as files
from random import randint as random
read = open("path.txt", "r")
messages = open("messages.txt", "r").readlines()
lines = read.readlines()
cmd("git remote add origin " + lines[0])
path = lines[1]
cmd("cd " + path)
cmd("git add .")
cmd("git commit -m " + "\"" + messages[random(0, len(messages))] + "\"")
write = open("path.txt", "w")
write.write("")
read.close()
write.close()
cmd("git remote remove origin")
print("Finished")
