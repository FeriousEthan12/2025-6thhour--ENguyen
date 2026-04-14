#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: HW_R7


#1. Create a class containing a def function that inits self and the three attributes: name, grade, color.
class student:
    def __init__(self,name, grade, color):
        self.name = name
        self.grade = grade
        self.color = color

    def next_year(self):
        self.grade += 1
        if self.grade == 13:
            print(f"{self.name} has graduated")

    def new_color(self):
        self.color = input("Enter your favorite color : ")
#2. Make a def function within the class that adds 1 to the grade attribute to any object called to it.
#If they are 12th grade, have the code change their grade to "graduated" instead.

#3. Make a def function within the class that offers the user to input/change their favorite color.

Ethan = student("Ethan", 9, "red")
print(f"{Ethan.name}'s grade is {Ethan.grade}")
Ethan.next_year()
print(f"{Ethan.name}'s next grade is {Ethan.grade}")
Ethan.new_color()
print(f"{Ethan.name}'s favorite color is {Ethan.color}")