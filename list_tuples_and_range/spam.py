menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'tomato']
]

for meal in menu:
    if 'spam' not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print("{0} has a spam core {1}"
              .format(meal, meal.count("spam")))
    print(", ".join(meal))
