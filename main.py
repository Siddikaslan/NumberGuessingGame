import random
from shape import shape

print(shape)
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.")

guessed_number = random.randint(1,100)
player_health = 0
game_status = True

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    player_health = 10
else:
    player_health = 5

while player_health > 0:
    print(f"You have {player_health} attempts remaining to guess the number.")
    player_gues = int(input("Make a guess: "))
    if player_gues == guessed_number:
        print("You win. Refresh the page to run again.")
        break
    elif player_gues < guessed_number:
        print("Too low.\nGuess again.")
    elif player_gues > guessed_number:
        print("Too high.\nGuess again.")
    player_health -= 1

if player_health == 0:
    print("You've run out of guesses. You lose. Refresh the page to run again.")
