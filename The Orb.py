import random

question = input("Do you want to ask the orb (y/n): ")
while True:
    if question == "y":
        responses = ["Sure", "That is burned into fate", "HECK YEA", "Yes and times it by 100", "Sure?",
                     "That seems ok", "nah", "HECK NO", "Don't ask me that again", "...", "What? I wasn't listening ", "nooooooooo"]
        print(random.choice(responses))
        question = input("Do you want to ask the orb (y/n): ")
    elif question == "n":
        print("Thank you for playing!")
        break
    else:
        print("What???")
        question = input("Do you want to ask the orb (y/n): ")