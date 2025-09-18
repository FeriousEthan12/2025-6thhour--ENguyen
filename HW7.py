#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello world!")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
Number_dictionary = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
}
#3. Print the keys of the dictionary from #2.
print(Number_dictionary)
#4. Print the values of the dictionary from #2
print(Number_dictionary.values())
#5. Print one of the three numbers from the list by itself
print(Number_dictionary["one"])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
Number_dictionary.update({"four" : 4})
#7. Print the entire dictionary from #2 with the updated key and value.
print(Number_dictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
Class = {"Student_1" : {"Name" : "Kash",
                        "Grade" : 12,
                        "In Esport" : False},
         "Student_2" : {"Name" : "Tristan",
                        "Grade" : 9,
                        "In Esport" : False},
         "Student_3" : {"Name" : "Greg",
                        "Grade" : 12,
                        "In Esport" : False
                        }
    ,}
#9. Print the names of all three classmates on the same line.
print(Class["Student_1"]["Name"], Class["Student_2"]["Name"], Class["Student_3"]["Name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
Class.pop("Student_1")
print(Class)

