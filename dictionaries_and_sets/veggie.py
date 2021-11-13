fruit = {"orange": "a sweet orange, citrus, fruit",
         "apple": "good for makind cider",
         "lemon": "a sour yellow cirtrus fruit",
         "grape": "a small, sweet, growing in bunches",
         "lime":  "a sour, green citrus fruit",
         }

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmm, lovely",
       "spinach": "can i have some more fruit please"
       }


print(veg)

veg.update(fruit)
print(veg)

print(fruit.update(veg))
print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty = veg

print(nice_and_nasty)
print(veg)
print(fruit)