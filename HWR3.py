#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: HW-R3


#1. import random and print "Hello World!"
import random
print("Hello World!")
#2. Create three variables that each randomly generate an integer between 1 and 10, print each number on the same line.
r = random.randint(1,10)
a = random.randint(1,10)
n = random.randint(1,10)
print(r,a,n)
#3. Create a list containing 5 strings listing 5 colors.
colour = ["Red", "Orange", "Yellow", "Green","Blue"]
#4. Use a function to randomly choose one of the 5 colors from the list and print the result.
print(random.choice(colour))
#5. Create an if statement that determines which of the three variables from #2 is the lowest.
if r < a and r < n:
    print(f"{r} is the lowest number")
elif a < n and a < r:
    print(f"{a} is the lowest number")
elif n < r and n < a:
    print(f"{n} is the lowest number")
else:
    print("2 numbers or more are the lowest number")