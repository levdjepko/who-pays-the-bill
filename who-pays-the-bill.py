import random


# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(",")

#print all the names
print (names)
randomNumber = random.randint(0, len(names) - 1) #get the random number
print (f"{names[randomNumber]} is going to pay the bill today!") #this person pays!


