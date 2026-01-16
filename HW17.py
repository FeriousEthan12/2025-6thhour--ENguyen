#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: HW17
import random
import time

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

def retry():
    ask = input("Would you like to try again? (y/n): ")
    if ask == "y" or ask == "Y":
        game()
    elif ask == "n" or ask == "N":
        print("Thank you for playing")


def opponent():
    random.randint(1,3)

def rock():
    if opponent == 1:
        print("Rock vs Rock")
        time.sleep(0.5)
        print("Draw")
        game()
    elif opponent == 2:
        print("Rock vs Paper")
        time.sleep(0.5)
        print("You Lose")
    else:
        print("Rock vs Scissor")
        time.sleep(0.5)
        print("You Win")
    retry()

def paper():
    if opponent == 1:
        print("Paper vs Rock")
        time.sleep(0.5)
        print("You Win")
        game()
    elif opponent == 2:
        print("Paper vs Paper")
        time.sleep(0.5)
        print("Draw")
    else:
        print("Paper vs Scissor")
        time.sleep(0.5)
        print("You Lose")
    retry()


def scissor():
    if opponent == 1:
        print("Scissor vs Rock")
        time.sleep(0.5)
        print("You Lose")
    elif opponent == 2:
        print("Scissor vs Paper")
        time.sleep(0.5)
        print("You Win")
    else:
        print("Scissor vs Scissor")
        time.sleep(0.5)
        print("Draw")
    retry()


def game():
    choice = int(input("Rock(1), Paper(2), or Scissor(3): "))
    if choice == 1:
        print("...")
        time.sleep(0.9)
        opponent()
        rock()
    elif choice == 2:
        print("...")
        time.sleep(0.9)
        opponent()
        paper()
    elif choice == 3:
        print("...")
        time.sleep(0.9)
        opponent()
        scissor()
    else:
        print("Try again")
        game()

game()



#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.













