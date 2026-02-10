#Name:Ethan Nguyen
#Class: 6th Hour
#Assignment: HW19

#1. Import the def functions created in problem 1-4 from HW16
from HW16 import hello, average, animal_list, loop

#2. Call the functions here and run HW19
hello()
average(int(input("Enter the number: ")), int(input("Enter the number: ")), int(input("Enter the number: ")))
animal_list("dog", "cat", "seal", "bird", "duck")
loop(int(input("Enter the max number: ")))

#3. Delete all calls for problem 5 in HW16 and run HW19 again.

#4. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello World!")

#5. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    num = int(input("Enter the number: "))
    div = (100/num)
    print(div)
except ZeroDivisionError:
    print("You can't divide by zero!")

#6. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    ask = int(input("Enter the number: "))
    print(ask)
except ValueError:
    print("You need to enter a integer")

#7. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
i = 6

while i > 0:
    i -= 1
    print(i)
    if i <= 0:
        raise Exception("i is less than 0")






