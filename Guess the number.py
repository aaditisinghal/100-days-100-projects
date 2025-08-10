print('''  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
          / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
         / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
         \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|        ''')
import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_integer = random.randint(1, 100)
choose=input("Choose a difficulty. Type 'easy' or 'hard':").lower()

for attempt in range(10, 0, -1):
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess < random_integer:
        print("Too low.\nGuess again.")
    elif guess > random_integer:
        print("Too high.\nGuess again.")
    else:
        print(f"You got it! The answer was {random_integer}.")
        break

    if attempt == 1:
        print(f"You've run out of guesses. The number was {random_integer}.")
