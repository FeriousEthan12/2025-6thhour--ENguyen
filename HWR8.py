#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: HW_R8


#1. Import all of HW_R7 into this assignment using the from/import function.
from HWR7 import student
#2. Create an object of three students in the classroom. Ask for their name, grade, and favorite color as need be.
Connor = student("Connor", 11, "Yellow")
Shane = student("Shane", 12, "Red")
Greg = student("Greg", 12, "Purple")
#3. Print the name of the first student.
print(Connor.name)
#4. Use the def function from HW_R7 to bump the grade level of the second student up by 1. Print the new grade.
Shane.next_year()
print(Shane.grade)
#5. Use the def function from HW_R7 to ask the third student to change their favorite color to something else.
#Print the new color.
Greg.new_color()
print(Greg.color)