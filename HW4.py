#Name:Ethan Nguyen
#Class: 6th Hour
#Assignment: HW4


#1. Print Hello World!
print("Hello World")
#1. Create a list with 5 strings containing 5 different names in it.
str_List = ["George", "John", "Smith", "Joseph", "Roger"]
print(str_List)
#2. Append a new name onto the Name List.
str_List.append("Jack")
print(str_List)
#3. Print out the 4th name on the list.
print(str_List[3])
#4. Create a list with 4 different integers in it.
int_List = [120, 23, 31, 74]
print(int_List)
#5. Insert a new integer into the 2nd spot and print the new list.
int_List.insert(1, 2)
print(int_List)
#6. Sort the list from lowest to highest and print the sorted list.
int_List.sort()
print(int_List)
#7. Add the 1st three numbers on the sorted list together and print the sum.
print(int_List[0] + int_List[1] + int_List[2])
#8. Create a list with two strings, two variables, and two boolean values.
many_List = ["damage", "Hurt", 10, 20, True, False]
print(many_List)
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(many_List[int(input())])