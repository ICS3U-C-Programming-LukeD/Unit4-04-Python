#!/usr/bin/env python3

# Created By: Luke Di Bert
# Date: April 23, 2025

# adds random module
import random

def main():
    rand = random.randint(0, 9)
    print(rand)
    while True:
        user_inp = input(str("Guess a number from 0 to 9: "))
        try:
            user_inp = int(user_inp)
            if user_inp == rand:
                print("You guessed correctly!")
                break
            elif user_inp != rand:
                print(user_inp, "was wrong, try again")
        except:
            print(user_inp, "is not a valid integer")


if __name__ == "__main__":
    main()
