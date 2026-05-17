#Python number guessing game

import random

while True:
    difficulty = input("Enter your difficulty (Easy, Medium, Hard): ").lower()

    if difficulty == "easy":
                print("------EASY🙂------")

                lowest_num = 1
                highest_num = 100
                answer = random.randint(lowest_num, highest_num)
                guesses = 0
                is_running = True
                attempts = 15
                print("----------------------------")
                print("Python Number Guessing Game")
                print("----------------------------")
                print(f"Select a number {lowest_num} and {highest_num}")

                while is_running:

                    guess = input("Enter your guess: ")
                    if guess.isdigit():
                        guess = int(guess)
                        guesses += 1
                        attempts -= 1

                        if guess < lowest_num or guess > highest_num:
                            print("That number is out of range")
                            print(f"Please select a number between {lowest_num} and {highest_num}")
                        elif attempts == 0:
                            print("Max attempts!")
                            print("-------YOU LOSE🥱------")
                            is_running = False
                        elif guess < answer:
                            print("Too low try again!")
                            print(f"You have {attempts} attempts ")
                        elif guess > answer:
                            print("Too high try again!")
                            print(f"You have {attempts} attempts ")
                        else:
                            print("---------WIN😎---------")
                            print(f"CORRECT! The answer was {answer}")
                            print(f"Number of guesses: {guesses} ")    
                            print(f"Remaining attempts: {attempts} ")
                            is_running = False        
                    else:
                        print("Invalid guess")
                        print(f"Please select a number between {lowest_num} and {highest_num}")
    elif difficulty == "medium":
                print("------MEDIUM😐------")
                lowest_num = 1
                highest_num = 500
                answer = random.randint(lowest_num, highest_num)
                guesses = 0
                is_running = True
                attempts = 12

                print("Python Number Guessing Game")
                print(f"Select a number {lowest_num} and {highest_num}")

                while is_running:

                    guess = input("Enter your guess: ")
                    if guess.isdigit():
                        guess = int(guess)
                        guesses += 1
                        attempts -= 1

                        if guess < lowest_num or guess > highest_num:
                            print("That number is out of range")
                            print(f"Please select a number between {lowest_num} and {highest_num}")
                        elif attempts == 0:
                            print("Max attempts!")
                            print("-------YOU LOSE🥱------")
                            is_running = False
                        elif guess < answer:
                            print("Too low try again!")
                            print(f"You have {attempts} attempts ")
                        elif guess > answer:
                            print("Too high try again!")
                            print(f"You have {attempts} attempts ")
                        else:
                            print("---------WIN😎---------")
                            print(f"CORRECT! The answer was {answer}")
                            print(f"Number of guesses: {guesses} ")    
                            print(f"Remaining attempts: {attempts} ")
                            is_running = False        
                    else:
                        print("Invalid guess")
                        print(f"Please select a number between {lowest_num} and {highest_num}")

    elif difficulty == "hard":
                print("------HARD😫------")
                lowest_num = 1
                highest_num = 1000
                answer = random.randint(lowest_num, highest_num)
                guesses = 0
                is_running = True
                attempts = 10

                print("Python Number Guessing Game")
                print(f"Select a number {lowest_num} and {highest_num}")

                while is_running:

                    guess = input("Enter your guess: ")
                    if guess.isdigit():
                        guess = int(guess)
                        guesses += 1
                        attempts -= 1

                        if guess < lowest_num or guess > highest_num:
                            print("That number is out of range")
                            print(f"Please select a number between {lowest_num} and {highest_num}")
                        elif attempts == 0:
                            print("Max attempts!")
                            print("-------YOU LOSE🥱------")
                            is_running = False
                        elif guess < answer:
                            print("Too low try again!")
                            print(f"You have {attempts} attempts ")
                        elif guess > answer:
                            print("Too high try again!")
                            print(f"You have {attempts} attempts ")
                        else:
                            print("---------WIN😎---------")
                            print(f"CORRECT! The answer was {answer}")
                            print(f"Number of guesses: {guesses} ")    
                            print(f"Remaining attempts: {attempts} ")
                            is_running = False        
                    else:
                        print("Invalid guess")
                        print(f"Please select a number between {lowest_num} and {highest_num}")

    else:
        print("Invalid Difficulty! ")
    print()
    play_again = input("Wanna Restart (y/n): ")
    if play_again == "n":
         print("-------THANKS FOR PLAYING-------")
         break
    else:
        continue