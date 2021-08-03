
import random 
number = random. randint(1,9)

print("Number Guessing")


chances = 0

while chances < 5:

    guess = int(input("Guess a number (between 1 and 9) "))

    if guess == number:
        print("Congratulations You Won!!!")
        break

    elif guess < number:
        print("Your guess is too low")
        
    else:
        print('Your guess is too high')

    chances = chances + 1

if not chances < 5:
    print("YOU LOSE!!! The number is", number)

