import random

def parse_input(string):
    return (0, 0, 0, 0)

# The number of correct colors at the correct place
def correct_color_and_place(guess, secret):
    count = 0

    return count

# The number of correct colors at the wrong place. Careful
# a correct color at the right place does not count here!
# Additionally, each color may be at the wrong place only once!
def correct_color(guess, secret):
    count = 0

    return count

def mastermind():
    secret = (random.randrange(1, 7),
              random.randrange(1, 7),
              random.randrange(1, 7),
              random.randrange(1, 7),)
    print(secret)

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
    assert(correct_color((1, 2, 3, 4), (4, 5, 6, 6)) == 1)
    assert(correct_color((4, 2, 3, 4), (4, 5, 6, 6)) == 1)
    assert(correct_color((4, 4, 3, 4), (4, 5, 6, 6)) == 1)
    assert(correct_color((4, 4, 3, 4), (4, 5, 3, 6)) == 2)
    print("Done")

test()

mastermind()
