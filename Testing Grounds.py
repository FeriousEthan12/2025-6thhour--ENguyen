'''
def dev_tool():
    dev = input("Type in a enemy's name to change the damage (Slime, Skeleton, Ork, Dire Wolf, King Calcium) : ")
ask = False

z = input("Do you want Dev Tools? (Yes or No) : ")
if z == "Yes" or z == "yes":
    ask = True
else:
    print("Thank you")

if ask == True:
    dev_tool()
'''


def dev_tool(enemy):
    print(enemy, "has been chosen")

dev_tool("Slime")