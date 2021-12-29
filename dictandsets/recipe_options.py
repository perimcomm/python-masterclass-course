recipes_tuple = {
    "Chicken and chips": [
        ("chicken", 100),
        ("popatoes", 3),
        ("salt", 1),
        ("malt vinegar", 5),
    ],
}

recipes_dict = {
    "Chicken and chips": {
        "chicken": 100,
        "popatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
}

for recipe, ingredients in recipes_tuple.items():
    print(f"Ingredients for {recipe}")
    for ingredient, quantity in ingredients:
        print(ingredient, quantity, sep=',')

print()

for recipe, ingredients in recipes_dict.items():
    print(f"Ingredients for {recipe}")
    for ingredient, quantity in ingredients.items():
        print(ingredient, quantity, sep=',')
    