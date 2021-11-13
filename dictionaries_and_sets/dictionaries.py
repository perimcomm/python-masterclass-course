fruit = {"orange": "a sweet orange, citrus, fruit",
         "apple": "good for makind cider",
         "lemon": "a sour yellow cirtrus fruit",
         "grape": "a small, sweet, growing in bunches",
         "lime":  "a sour, green citrus fruit",
         }

print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))

