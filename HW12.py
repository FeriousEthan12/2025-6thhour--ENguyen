#Name:Ethan Nguyen
#Class: 6th Hour
#Assignment: HW12

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.

i = 5
while i > 0:
    print(i)
    i -= 1
else:
    print("Hello World")

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
j = 1
while j <= 30:
    j += 1
    if j % 2 == 0:
        print(j)

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
k = 0
while k < 30:
    k += 1
    if k % 3 == 0:
        continue
    print(k)

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
import random
l = random.randint(1,6)
while True:
    print(l)
    if l == 1:
        break
    else:
        l = random.randint(1,6)

#5. Create a while loop that asks for a number input until the user inputs the number 0.
m = int(input("Type a number: "))
while True:
    if m == 0:
        break
    else:
        m = int(input("Type a number: "))