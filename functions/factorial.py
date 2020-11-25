def calculate_factorial(number):
    if number <= 1:
        return 1

    return number * calculate_factorial(number - 1)


print(calculate_factorial(4))
print(calculate_factorial(5))
