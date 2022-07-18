from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got the answer! It was {answer}.")

# Difficulty Function
def difficulty():
    difficulty = input('Pick a difficulty. Easy or Hard. ')
    if difficulty == 'easy' or 'Easy':
        return EASY_LEVEL_TURNS
    elif difficulty == 'hard' or 'Hard':
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print('Welcome to the Number Guessing Game.')
    print("I'm thinking of a number between 1 and 100.")
    # Picking the random number
    answer = randint(1, 100)
    print(f'Psst, the answer is {answer}')

    turns = difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        # Make a guess
        guess = int(input('Make a guess: '))

        #Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You lose.")
            return
        elif guess != answer:
            print("Guess again.")
difficulty()
game()