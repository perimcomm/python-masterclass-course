import random
highest = 10
answer = random.randint(1, highest)
guess = 0
print(answer) # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())
    if guess == answer:
        print("You are correct")
        break
    else:
        if guess < answer:
            print("Guess Higher")
        else:
            print("Guess lower")
