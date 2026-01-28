#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def hi():
    print("Hello World!")

#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def flip():
    global heads, tails
    for i in range (1, 101):
        flip = random.randint(1, 2)
        if flip == 1:
            heads += 1
        else:
            tails += 1


#4. Call the "Hello world" and "Coin Flip" functions here
hi()
flip()
#5. Print the final result of heads and tails here
print("Heads:", heads)
print("Tails:", tails)
#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["black", "red", "green", "purple", "brown"]
#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def bean():
    print(beanBag)
    remove = random.choice(beanBag)
    beanBag.remove(remove)
    print (f"You nabbed a {remove} beans")
    print(beanBag)

#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def bean2():
    ask = input("Would you like to get another bean? (y/n): ")
    if ask == "y" or ask == "Y":
        if beanBag == []:
            print("No beans")
        else:
            bean()
            bean2()
    elif ask == "n" or ask == "N":
        print("No more beans for you!")
    else:
        print("Try again!")
        bean2()

#9. Call the "Bean Pull" function here
bean()
bean2()