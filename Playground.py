#Name :Ethan Nguyen
#Class: 6th Hour
#Assignment: Playground

import random

D6 = random.randint(1,6)
D20 = random.randint(1,20)


enemy = ["skeleton", "ork", "dragon", "ghoul"]

#print("You encounter a", random.choice(enemy))
#print(input("What do you do?"))


#print(input("What is your name"))

str = [random.randint(1,6),random.randint(1,6) ,random.randint(1,6) ,random.randint(1,6)]
str.sort()

dex = [random.randint(1,6),random.randint(1,6) ,random.randint(1,6) ,random.randint(1,6)]
dex.sort()

con = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
con.sort()

int = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
int.sort()

wis = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
wis.sort()

cha = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
cha.sort()

stat = {"Str" :  str[1] + str[2] + str[3],
        "Dex" : dex[1] + dex[2] + dex[3],
        "Con" : con[1] + con[2] + con[3],
        "Int" : int[1] + int[2] + int[3],
        "Wis" : wis[1] + wis[2] + wis[3],
        "Cha" : cha[1] + cha[2] + cha[3],}



print(stat)