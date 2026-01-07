#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Type a number: "))
b = int(input("Type another number: "))
c = int(input("I swear this is the last number: "))
#4. Add a and b together, then divide the sum by c. Print the result.
abc = (a + b) / c
print(abc)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print(round(abc))
if abc % 2 == 0:
    print("Even")
else:
    print("Odd")
#6. Create a list of five different random integers between 1 and 10.
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#7. Print the 4th number in the list.
print(num_list)
print(num_list[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
num_list.append(random.randint(1, 10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
num_list.sort()
print(num_list)
print(num_list[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 0
while i < 100:
    i += 1
    print(i)
#11. Create a list containing the names of five other students in the classroom.
student_list = ["Connor", "Kash", "Shane", "Ally", "Greg"]
#12. Create a for loop that individually prints out the names of each student in the list.
for s in student_list:
    print(s)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for n in range(1,101):
    print(n)
    if n % 10 == 0:
        break
#14. Free space. Do something creative. :)

question = input("Do you want to ask the orb (y/n): ")
while True:
    if question == "y":
        responses = ["Sure", "That is seared into fate", "HECK YEA", "Do that and times it by 100", "Sure?", "That seems ok", "nah", "HECK NO", "Don't ask me that again", "...", "What? I wasn't listening ",
                     "nooooooooo"]
        print(random.choice(responses))
        question = input("Do you want to ask the orb (y/n): ")
    elif question == "n":
        print("Thank you for playing!")
        break
    else:
        print("What???")
        question = input("Do you want to ask the orb (y/n): ")