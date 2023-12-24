from random import randint
easy_attempts= 10
hard_attempts= 5

def check_answer(guess, answer, attempts):
    '''check answer and return the attempts'''
    if guess> answer:
        print("Too high.")
        return attempts-1
    elif guess < answer: 
        print("Too low.")
        return attempts -1
    else:
        print(f"You got it! The answer was{answer}")
        


def set_difficulty():
    level= input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        return easy_attempts
    else:
        return hard_attempts
def game():
    print("Welcome to the Number Guessing Game")
    print("I m thinking of a nuber between 1 to 100")
    answer =randint(1,100)

    guess=0
    attempts = set_difficulty()
    while guess!= answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        
        check_answer(guess, answer, attempts)
        if attempts== 0:
            print("you have lose. return back")
            return
        elif guess!= answer:
            print("guess again")

game()