import random

# Given a string of 4 integers between 1 and 6, return
# the 4-tuple containing said integers.

def parse_input(string):

    # Write code here!

    return (0, 0, 0, 0)

# The number of correct colors at the correct place of the
# input guess compared to the given secret.

def correct_color_and_place(guess, secret):
    count = 0

    # Write code here!

    return count

# The number of correct colors at the wrong place. Careful
# a correct color at the right place does not count here!
# Additionally, count only one correct color at the wrong place
# per place in the solution. So having two 1's in the guess at
# the wrong place, but only one 1 in the solution, can only count
# one of the 1's in the guess as correct color but wrong place, the 
# second 1 in the guess is wrong. So
#  correct_color((5, 6, 1, 1), (1, 2, 3, 4))
# should return 1, not 2.

def correct_color(guess, secret):
    count = 0

    # Write code here!

    return count

# Play mastermind! It should ask the user for a guess exactly
# 13 times and report on the correct color & places and just the
# correct color in each round. If the player guesses the secret,
# print conrajulatyns! and end the game.

def mastermind():
    secret = (random.randrange(1, 7),
              random.randrange(1, 7),
              random.randrange(1, 7),
              random.randrange(1, 7),)

    # Write code here!

    return

ROUND  = 0
SECRET = None

# We extend the mastermind game with a step-function. This function
# is called with a parsed guess (so a tuple), and returns the amount
# of red and white pins as a tuple: (white_pins, red_pins). It also
# increments the global variable ROUND and in the very first round it
# chooses a random secret and saves it in SECRET.
# 
# This leaves an open question, how do we know that we have won?

def mastermind_step(guess):
    global ROUND, SECRET

    # Write code here!
    
    return (white_pins, red_pins)

# Playing is boring, let the computer play for you. Using the function
# mastermind_step, guess the secret by simply guessing every 4-tuple
# there is. Don't worry about runtime, we do not care about the rounds
# it takes (yet).

def bruteforce():

# Test that the functions where correctly implemented.

def test():
    print("Testing parse_input")
    assert(parse_input("1234") == (1, 2, 3, 4))
    assert(parse_input("4444") == (4, 4, 4, 4))
    assert(parse_input("6425") == (6, 4, 2, 5))
    print("Done")

    print("Testing correct_color_and_place")
    assert(correct_color_and_place((1, 2, 3, 4), (4, 5, 6, 6)) == 0)
    assert(correct_color_and_place((4, 2, 3, 4), (4, 5, 6, 6)) == 1)
    assert(correct_color_and_place((4, 4, 3, 4), (4, 5, 6, 6)) == 1)
    assert(correct_color_and_place((4, 4, 3, 4), (4, 5, 3, 6)) == 2)
    print("Done")

    print("Testing correct_color")
    assert(correct_color((4, 2, 3, 4), (4, 5, 6, 6)) == 0)
    assert(correct_color((1, 2, 3, 4), (4, 5, 6, 6)) == 1)
    assert(correct_color((4, 4, 5, 4), (4, 5, 6, 6)) == 1)
    assert(correct_color((4, 6, 3, 5), (4, 5, 3, 6)) == 2)
    print("Done")

    print("Testing mastermind_step")
    global SECRET, ROUND
    SECRET = (1, 2, 3, 4)
    ROUND = 3
    assert(mastermind_step((1, 2, 3, 4)) == (4, 0))
    assert(mastermind_step((3, 2, 9, 4)) == (2, 1))
    assert(mastermind_step((2, 1, 4, 4)) == (1, 2))
    SECRET = None
    ROUND = 0
    mastermind_step((2, 1, 4, 4))
    assert(SECRET is not None)

    # Recreate the default state
    SECRET = None
    ROUND = 0
    print("Done")

test()
