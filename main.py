from os import system as cmd
from os.path import dirname as path
from os import listdir as files
read = open("path.txt", "r")
cmd("git remote add origin " + read.readlines()[0])
path = path(read.readlines()[1])
write = open("path.txt", "w")
write.write("")
read.close()
write.close()
cmd("git remote remove origin")
print("Finished")
