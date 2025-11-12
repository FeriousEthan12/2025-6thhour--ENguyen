enemy = {"Slime" : {"passive" : "slimy",
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
Dev = input("Type in a ememy's name to change the damage (Slime, Skeleton, Ork, Dire Wolf, King Calcium) : ")

if Dev == "Slime":
    print("Damage :", enemy["Slime"]["Damage"])
    print(enemy["Slime"].update({"Damage" : int(input("Change Slime damage : "))}))
    print(enemy["Slime"])
if Dev == "Skeleton":
    print("Damage :",enemy["Skeleton"]["Damage"])
    print(enemy["Skeleton"].update({"Damage" : int(input("Change Skeleton damage : "))}))
    print(enemy["Skeleton"])
if Dev == "Ork":
    print("Damage :",enemy["Ork"]["Damage"])
    print(enemy["Ork"].update({"Damage" : int(input("Change Ork damage : "))}))
    print(enemy["Ork"])
if Dev == "Dire Wolf":
    print("Damage :",enemy["Dire Wolf"]["Damage"])
    print(enemy["Dire Wolf"].update({"Damage" : int(input("Change Dire Wolf damage : "))}))
    print(enemy["Dire Wolf"])
if Dev == "King Calcium":
    print("Damage :",enemy["King Calcium"]["Damage"])
    print(enemy["King Calcium"].update({"Damage" : int(input("Change King Calcium's damage : "))}))
    print(enemy["King Calcium"])


#Old Dev Tool
'''
print(enemy)
enemy["Slime"].update({"Damage" : int(input("Slime Damage Changed? "))})
print("Slime Damage :", enemy["Slime"]["Damage"])
enemy["Skeleton"].update({"Damage" : int(input("Skeleton Damage Changed? "))})
print("Skeleton Damage :", enemy["Skeleton"]["Damage"])
enemy["Ork"].update({"Damage" : int(input("Ork Damage Changed? "))})
print("Ork Damage :", enemy["Ork"]["Damage"])
enemy["Dire Wolf"].update({"Damage" : int(input("Dire Wolf Damage Changed? "))})
print("Dire Wolf Damage :", enemy["Dire Wolf"]["Damage"])
enemy["King Calcium"].update({"Damage" : int(input("King Calcium Damage Changed? "))})
print("King Calcium Damage :", enemy["King Calcium"]["Damage"])
'''