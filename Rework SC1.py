
#The enemy list
enemy = {
    "Slime" : {"passive" : "slimy",
                    "HP" : 20,
                    "Damage" : 10,
                    "Move" : "SlimeBall"},
    "Skeleton" : {"passive" : "Hollow",
                       "HP" : 50,
                        "Damage" : 25,
                       "Move" : "Swing"},
    "Ork" : {"passive" : "ToughSkin",
                  "HP" : 80,
                  "Damage" : 50,
                  "Move" : "Monster's Roar"},
    "Dire Wolf" : {"passive" : "Pack",
                        "HP" : 30,
                        "Damage" : 60,
                        "Move" : "Call Pack"},
    "King Calcium" : {"passive" : "Marrow Defence",
                           "HP" : 125,
                            "Damage" : 100,
                           "Move" : "Bone Spear"},
         }


#New reworked Dev Tool

dev_tool = True

Dev = input("Type in a enemy's name to change the damage (Slime, Skeleton, Ork, Dire Wolf, King Calcium) : ")
while dev_tool == True:
    if Dev == "Slime":
        print("Damage :", enemy["Slime"]["Damage"])
        enemy["Slime"].update({"Damage": int(input("Change Slime damage : "))})
        print(enemy["Slime"])
        dev_tool = False
        Dev = input("Would you like to change another enemy's damage? (Y/N) : ")
        if Dev == "Y" or Dev == "y":
            dev_tool = True
        else:
            print("Thank you")
    elif Dev == "Skeleton":
        print("Damage :", enemy["Skeleton"]["Damage"])
        enemy["Skeleton"].update({"Damage": int(input("Change Skeleton damage : "))})
        print(enemy["Skeleton"])
        dev_tool = False
        Dev = input("Would you like to change another enemy's damage? (Y/N) : ")
        if Dev == "Y" or Dev == "y":
            dev_tool = True
        else:
            print("Thank you")
    elif Dev == "Ork":
        print("Damage :", enemy["Ork"]["Damage"])
        enemy["Ork"].update({"Damage": int(input("Change Ork damage : "))})
        print(enemy["Ork"])
        dev_tool = False
        Dev = input("Would you like to change another enemy's damage? (Y/N) : ")
        if Dev == "Y" or Dev == "y":
            dev_tool = True
        else:
            print("Thank you")
    elif Dev == "Dire Wolf":
        print("Damage :", enemy["Dire Wolf"]["Damage"])
        enemy["Dire Wolf"].update({"Damage": int(input("Change Dire Wolf damage : "))})
        print(enemy["Dire Wolf"])
        dev_tool = False
        Dev = input("Would you like to change another enemy's damage? (Y/N) : ")
        if Dev == "Y" or Dev == "y":
            dev_tool = True
        else:
            print("Thank you")
    elif Dev == "King Calcium":
        print("Damage :", enemy["King Calcium"]["Damage"])
        enemy["King Calcium"].update({"Damage": int(input("Change King Calcium's damage : "))})
        print(enemy["King Calcium"])
        dev_tool = False
        Dev = input("Would you like to change another enemy's damage? (Y/N) : ")
        if Dev == "Y" or Dev == "y":
            dev_tool = True
        else:
            print("Thank you")

    else:
        print("Invalid input")
        Dev = input("Type in a enemy's name to change the damage (Slime, Skeleton, Ork, Dire Wolf, King Calcium) : ")









#Old Dev Tool

#print(enemy)
#enemy["Slime"].update({"Damage" : int(input("Slime Damage Changed? "))})
#print("Slime Damage :", enemy["Slime"]["Damage"])
#enemy["Skeleton"].update({"Damage" : int(input("Skeleton Damage Changed? "))})
#print("Skeleton Damage :", enemy["Skeleton"]["Damage"])
#enemy["Ork"].update({"Damage" : int(input("Ork Damage Changed? "))})
#print("Ork Damage :", enemy["Ork"]["Damage"])
#enemy["Dire Wolf"].update({"Damage" : int(input("Dire Wolf Damage Changed? "))})
#print("Dire Wolf Damage :", enemy["Dire Wolf"]["Damage"])
#enemy["King Calcium"].update({"Damage" : int(input("King Calcium Damage Changed? "))})
#print("King Calcium Damage :", enemy["King Calcium"]["Damage"])
