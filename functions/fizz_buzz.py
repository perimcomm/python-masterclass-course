def fizz_buzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return "fizz busss"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "fizz "


test = 16
for i in range(1, 25):
    print("The function returned", fizz_buzz(i))


