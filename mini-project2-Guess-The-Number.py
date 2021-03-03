"""
Week 2 Mini-Project of An Introduction to Interactive Programming

CodeSkulptor: https://py3.codeskulptor.org/#user305_U4TDlyK1ZQ_0.py
Written in Python 3
"""

# Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

num_range = 100
guess_remaining = 7
secret_num = random.randrange(0, num_range)

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    global guess_remaining
    global secret_num
    
    if num_range == 100:
        guess_remaining = 7
    else:
        guess_remaining = 10
     
    secret_num = random.randrange(0, num_range)
    
    print("New game. Range is from 0 to {}".format(str(num_range)))
    print("Number of remaining guesses is {}".format(str(guess_remaining)))


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100
    
    print()
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000

    print()
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global num_range
    global guess_remaining
    global secret_num
    
    guess_remaining -= 1
    if int(guess) == secret_num:
        print("\nGuess was {}".format(guess))
        print("Number of remaining guesses is {}".format(str(guess_remaining)))
        print("Correct!\n")
        
    elif int(guess) < secret_num:
        print("\nGuess was {}".format(guess))
        print("Number of remaining guesses is {}".format(str(guess_remaining)))
        
        if guess_remaining == 0:
            print("You ran out of guesses. The number was {}\n".format(str(secret_num)))
        else:
            print("Higher!")
        
    elif int(guess) > secret_num:
        print("\nGuess was {}".format(guess))
        print("Number of remaining guesses is {}".format(str(guess_remaining)))
        
        if guess_remaining == 0:
            print("You ran out of guesses. The number was {}\n".format(str(secret_num)))
        else:
            print("Lower!")
    
    # Start a new game when player win or lose
    if (guess_remaining == 0) or (int(guess) == secret_num):
        new_game()

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)


# call new_game 
new_game()

