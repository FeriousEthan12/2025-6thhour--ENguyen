#Name: Ethan Nguyen
#Class: 5th Hour
#Assignment: HW-R2


#1. Print "Hello World!"
print("Hello World!")
#2. Create an empty list.
nlist = []
#3. Create a list that contains the names of everyone in the classroom.
list = ["Connor", "Devon", "Alaya", "Shane", "Eli", "Ally", "Tristan", "Ethan", "Greg", "Kash", "Brodie"]
#4. Print the list from #3, sort the list, then print the list again.
print(list)
list.sort()
print(list)
#5. Append 5 different integers into the empty list from #2 and print the list.
nlist.append(5)
nlist.append(92)
nlist.append(32)
nlist.append(75)
nlist.append(1)
print(nlist)
#6. Add together the middle three numbers in the list from #2 and print the result.
print(nlist[1] + nlist[2] + nlist[3])
#7. Remove the very first number in the list from #2. Print the new first number.
nlist.remove(nlist[0])
print(nlist[0])
#8. Create a dictionary with three keys with respective values: your name, your grade, and your favorite color.
self = {"Name" : "Ethan",
        "Grade" : 9,
        "Color" : "Red"}
#9. Using the update function, add a fourth key and value determining your favorite candy.
self.update({"Candy" : "Chocolate"})
#10. Print ONLY the values of the dictionary from #8.
print(self["Name"], self["Grade"], self["Color"])