import random


def get_integer(prompt):
    """
    Gets an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The string that user will see, when
            they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

        print("{0} is not a valid number".format(temp))


highest = 10
answer = random.randint(1, highest)
guess = 0
print(answer)

print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")
    if guess == answer:
        print("You are correct")
        break
    else:
        if guess < answer:
            print("Guess Higher")
        else:
            print("Guess lower")
