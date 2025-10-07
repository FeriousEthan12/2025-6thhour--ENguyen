#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: HW9

import random

#1. Print "Hello World!"
print("Hello World!")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
rannum = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
#3. Print the list.
print(rannum)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if rannum[0] >= rannum[1] and rannum[0] >= rannum[2]:
    print(rannum[0])
elif rannum[1] >= rannum[0] and rannum[1] >= rannum[2]:
    print(rannum[1])
elif rannum[2] >= rannum[0] and rannum[2] >= rannum[1]:
    print(rannum[2])
#5. Tie the result (the largest number) from #4 to a variable called "num".
if rannum[0] >= rannum[1] and rannum[0] >= rannum[2]:
    num = (rannum[0])
elif rannum[1] >= rannum[0] and rannum[1] >= rannum[2]:
    num = (rannum[1])
elif rannum[2] >= rannum[0] and rannum[2] >= rannum[1]:
    num = (rannum[2])
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print(num, "is divisible by 2 and 3")
    else:
        print(num, "is divisible by 2")
elif num % 3 == 0:
    if num % 2 == 0:
        print(num, "is divisible by 2 and 3")
    else:
        print(num, "is divisible by 3")
else:
    print(num, "is not divisible by 2 or 3")