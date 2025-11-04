#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: HW13

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".
import time


#Create a while loop that follows the rules of the game.
FizzBuzz = 0
while FizzBuzz < 100:
    FizzBuzz += 1
    time.sleep(0.4)
    if FizzBuzz % 3 == 0 and FizzBuzz % 5 == 0:
        print("FizzBuzz")
    elif FizzBuzz % 5 == 0:
        print("Buzz")
    elif FizzBuzz % 3 == 0:
        print("Fizz")
    else:
        print(FizzBuzz)