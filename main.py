from os import system as cmd
cmd("git remote remove origin")
read = open("path.txt", "r")
cmd("git remote add origin " + read.readlines()[0])
write = open("path.txt", "w")
write.write("")
read.close()
write.close()
print("Finished")