#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.

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