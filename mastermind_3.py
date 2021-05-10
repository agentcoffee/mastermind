# If your previous file has a different name than 'mastermind.py' adjust it
# here:
from mastermind import correct_color, correct_color_and_place, mastermind_step

# Bruteforce takes too long. Write a solver for your mastermind_step function.
# It should be able to guess the secret correctly in under 5 tries. You can
# look up an efficient algorithm here
# en.wikipedia.org/wiki/Mastermind_(board_game).
#
# As a structure you could start by building a set (you can find python
# documentation on that) of all possible guesses and start your first try with
# a random guess. Then after you have an answer to your guess (correct color,
# correct color and place), you can check with the remaining set of guesses
# which guess would produce the same (correct color, correct color and place)
# answer together with your initial guess. In essence asking: "If that was the
# secret, would it produce the same answer i just received?". If not, then
# that's not a possible guess anymore. 
#
# You can reuse the functions correct_color() and correct_color_and_place()
# from before, they are already importet.

def solve():

    # Write code here !

    return

solve()
