#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: Scenario 6

import random, time

#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.
class stat_sheet:
    def __init__(self, HP, Init, AC, Atk, Damage):
        self.HP = HP
        self.Init = Init
        self.AC = AC
        self.Atk = Atk
        self.Damage = Damage

#Party members
LaeZel = stat_sheet(48,1,17,6, random.randint(1,6) + random.randint(1,6) + 3)
Shadowheart = stat_sheet(40,1,18,4, random.randint(1,6) + 3)
Gale = stat_sheet(32,1,14,6, random.randint(1,10) + random.randint(1,10))
Astarion = stat_sheet(40,3,14,5, random.randint(1,8) + random.randint(1,6) + 4)


#Enemies
Goblin = stat_sheet(7,0,12,4, random.randint(1,6) + 2)
Ork = stat_sheet(15,1,13,6, random.randint(1,12) + 3)
Troll = stat_sheet(84,1,15,7, random.randint(1,6) + random.randint(1,6) + 4)
Mindflayer = stat_sheet(71,1,15,7, random.randint(1,10) + random.randint(1,10) + 4)
Dragon = stat_sheet(127,2,18,7, random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4)




def Player_ATK():
    P_Atk =  random.randint(1,20)

    if P_Atk == 20:
        print("Nat 20!")
        time.sleep(1)
        Ork.HP -= LaeZel.Damage * 2
        print(LaeZel.Damage * 2, "Damage")
        time.sleep(0.4)
        print(f"Ork: {Ork.HP}")

    elif P_Atk == 1:
        print("Nat 1! ):")
        time.sleep(1)

    elif P_Atk + LaeZel.Atk > Ork.AC:
        time.sleep(0.4)
        print(f"You hit.({P_Atk + LaeZel.Atk})")
        Ork.HP -= LaeZel.Damage
        time.sleep(0.4)
        print(f"You do {LaeZel.Damage} damage")
        time.sleep(0.4)
        print(f"Ork: {Ork.HP}")

    elif P_Atk + LaeZel.Atk <= Ork.AC:
        time.sleep(0.4)
        print(f"You miss.({P_Atk + LaeZel.Atk})")



def Enemy_ATK():
    E_Atk = random.randint(1,20)

    if E_Atk == 20:
        print("THE ENEMY GOT A NAT 20")
        time.sleep(1)
        LaeZel.HP -= Ork.Damage * 2
        print(Ork.Damage * 2, "Damage")
        time.sleep(0.4)
        print(f"LaeZel: {LaeZel.HP}")

    elif E_Atk == 1:
        print("The enemy rolled a nat 1 ):")
        time.sleep(1)

    elif E_Atk + Ork.Atk > LaeZel.AC:
        time.sleep(0.4)
        print(f"The Ork hits.({E_Atk + Ork.Atk})")
        LaeZel.HP -= Ork.Damage
        time.sleep(0.4)
        print(f"The Ork does {Ork.Damage} damage")
        time.sleep(0.4)
        print(f"LaeZel: {LaeZel.HP}")

    elif E_Atk + Ork.Atk <= LaeZel.AC:
        time.sleep(0.4)
        print(f"The Ork missed.({E_Atk + Ork.Atk})")



def battle():
    p_roll = random.randint(1,20) + LaeZel.Init
    e_roll = random.randint(1,20) + Ork.Init

    time.sleep(0.4)


    if p_roll > e_roll:
        time.sleep(0.4)
        print("You go first")
        while LaeZel.HP >= 0 and Ork.HP >= 0:
            time.sleep(0.4)

            Player_ATK()
            if LaeZel.HP <= 0:
                print("You lose")
                exit()

            elif Ork.HP <= 0:
                print("You win")
                exit()
            Enemy_ATK()
            if LaeZel.HP <= 0:
                print("You lose")
                exit()

            elif Ork.HP <= 0:
                print("You win")
                exit()

    elif p_roll < e_roll:
        time.sleep(0.4)
        print("Enemy goes first")
        while LaeZel.HP >= 0 and Ork.HP >= 0:
            time.sleep(0.4)

            Enemy_ATK()
            if LaeZel.HP <= 0:
                print("You lose")
                exit()

            elif Ork.HP <= 0:
                print("You win")
                exit()
            Player_ATK()
            if LaeZel.HP <= 0:
                print("You lose")
                exit()

            elif Ork.HP <= 0:
                print("You win")
                exit()


    else:
        battle()




battle()

#(Translation: Rebuild Semester Project 1 using classes instead of dictionaries, include and refactor
#the combat test code below as well.)