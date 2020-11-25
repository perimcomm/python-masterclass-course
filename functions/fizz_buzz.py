def fizz_buzz(number: int) -> str:
    if number % 5 == 0 and number % 3 == 0:
        return "fizz busss"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "fizz "


input("Play Fizz Buzz. Press enter to start")
print()

next_number = 0

while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")

    if players_answer != correct_answer:
        print("You lose the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(players_answer))




