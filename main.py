### NOTE: ###
### The following code is a code-along with an instructor that was done after writing my own code (found in my 'guess-the-number' repository).
### It's only here to compare with my own code for study purposes. :)

from random import randint
from art import logo

print(logo)

answer = randint(1, 100)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game():
  #Function to check user's answer against actual answer:
  def check_answer(guess, answer, turns):
    if guess > answer:
      print("Too high.")
      return turns - 1
    elif guess < answer:
      print("Too low.")
      return turns - 1
    else:
      print(f"You got it! The answer was {answer}.")

  #Make function to set difficulty:
  def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'. ")
    if level == "easy":
      return EASY_LEVEL_TURNS
    else:
      return HARD_LEVEL_TURNS

  turns = set_difficulty()

  #Choosing a random number between 1 and 100:
  print("Welcome to the number guess game!")
  print("I'm thinking of a number between 1 and 100.")
  print(f"psss the answer is {answer}")
  

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining.")
  #Let the user guess a number:
    guess = int(input("Guess a number:  "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("GAME OVER")
      return
    elif turns != 0 and guess != answer:
      print("Guess again.")

game()