menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'tomato']
]

###Primeira Solucao
for meal in menu:
    if 'spam' in meal:
        meal.remove('spam')
    print(meal)

###Segunda Solucao
for meal in menu:
    for food in meal:
        if food != "spam":
            print(food)

