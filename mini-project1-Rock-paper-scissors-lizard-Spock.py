"""
Week 1 Mini-Project of An Introduction to Interactive Programming

CodeSkulptor: https://py3.codeskulptor.org/#user305_VL53XIvoyB_1.py
Written in Python 3
"""
# Rock-paper-scissors-lizard-Spock

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def name_to_number(name):
    """
    Inputs:
      name - A string that could be either rock, paper, scissors, lizard, or Spock.
      
    Ouput:
      Convert name to number and return an interger from 0 - 4.
    """
    
    # convert name to number using if/elif/else
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4


def number_to_name(number):
    """
    Inputs:
      number - An interger number from 0 - 4.
      
    Ouput:
      Convert interger number to name: rock, paper, scissors, lizard, or Spock.
      Then reutrn the name.
    """

    # convert number to a name using if/elif/else
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    

def rpsls(player_choice):
    """
    Inputs:
      player_choice - is a string of the form rock, paper, scissors, lizard or Spock.
      
    Ouput:
      Prints out the game.
      
      Player chooses {player_choice}
      Computer chooses {com_choice}
      Player wins!/ Computer wins!/ Player and computer tie!
    """

    # print a blank line to separate consecutive games
    print()

    # print out the message for the player's choice
    print("Player chooses {}".format(player_choice))

    # convert the player's choice to player_number using the function name_to_number()
    player_value = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    computer_value = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(computer_value)
    
    # print out the message for computer's choice
    print("Computer chooses {}".format(comp_choice))

    # compute difference of comp_number and player_number modulo five
    result = (player_value - computer_value) % 5

    # use if/elif/else to determine winner, print winner message
    if result == 0:
        print("Player and computer tie!")
    elif 0 < result < 3:
        print("Player wins!")
    else:
        print("Computer wins!")

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
