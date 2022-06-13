from os import system as cmd
from os.path import dirname as path
read = open("path.txt", "r")
cmd("git remote add origin " + read.readlines()[0])
path = path(____)
write = open("path.txt", "w")
write.write("")
read.close()
write.close()
cmd("git remote remove origin")
print("Finished")
