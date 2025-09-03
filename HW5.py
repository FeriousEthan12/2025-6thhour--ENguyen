#Name:Ethan Nguyen
#Class: 6th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
Num_list=[15,22,134,441,52,26,47,980,9]
print(Num_list)
#2. Sort the list from highest to lowest.
Num_list.sort()
print(Num_list)
#3. Create an empty list.
emp_list=[]
print(emp_list)
#4. Remove the median number from the first list and add it to the second list.
emp_list.append(Num_list[4])
print(emp_list)
Num_list.remove(Num_list[4])
print(Num_list)
#5. Remove the first number from the first list and add it to the second list.
emp_list.append(Num_list[0])
Num_list.remove(Num_list[0])
#6. Print both lists.
print(Num_list)
print(emp_list)
#7. Add the two numbers in the second list together and print the result.
print(emp_list[0] + emp_list[1])
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
Num_list.append(emp_list[0] + emp_list[1])
print(Num_list)
#9. Sort the first list from lowest to highest and print it.
Num_list.sort ()
print(Num_list)