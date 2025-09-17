#Name :Ethan Nguyen
#Class: 6th Hour
#Assignment: Playground

import random

D6 = random.randint(1,6)
D20 = random.randint(1,20)


enemy = ["skeleton", "ork", "dragon", "ghoul"]

#print("You encounter a", random.choice(enemy))
#print(input("What do you do?"))


print(input("What is your name"))

roll = [random.randint(1,6),random.randint(1,6) ,random.randint(1,6) ,random.randint(1,6) ]
roll.sort()
stat = roll[1] + roll[2] + roll[3]
print(stat)