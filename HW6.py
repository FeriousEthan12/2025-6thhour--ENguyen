#Name:Ethan Nguyen
#Class: 6th Hour
#Assignment: HW6


#1. Import the "random" library
import random
#2. print "Hello World!"
print("Hello world")
#3. Create three different variables that each randomly generate an integer between 1 and 10
Random_1 = random.randint(1,10)
Random_2 = random.randint(1,10)
Random_3 = random.randint(1,10)
Random_List = [Random_1,Random_2,Random_3]
#4. Print the three variables from #3 on the same line.
print(Random_1,Random_2,Random_3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
Add = Random_List[0] + 2
Sub = Random_List[1] - 4
Mult = Random_List[2] * 1.5
#6. Print each result from #5 on the same line.
print(Add, Sub, Mult)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
D6_stat = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#8. Sort the list in #7 and print it.
D6_stat.sort()
print(D6_stat)
#9. Add together the highest three numbers in the list from #7 and print the result.
print(D6_stat[1] + D6_stat[2] + D6_stat[3])
#10. Create a list with 5 names of other students in this class and print the list.
Class_list = ["Tristan", "Connor", "Cash", "Shawn", "Greg"]
print(Class_list)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(Class_list)
print(Class_list)
#12. Print a random choice from the list of names from #10.
print(random.choice(Class_list))