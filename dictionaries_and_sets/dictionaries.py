fruit = {"orange": "a sweet orange, citrus, fruit",
         "apple": "good for makind cider",
         "lemon": "a sour yellow cirtrus fruit",
         "grape": "a small, sweet, growing in bunches",
         "lime":  "a sour, green citrus fruit",
         }

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "and odd shaped apple"
# print(fruit)
# fruit["pear"] = "great with tequila"
# print(fruit)
# # del fruit["lemon"] #SE PASSAR SEM A KEY DELETA TODO O DICIONARIO
# # print(fruit)
# # fruit.clear() #ESVAZIA O DICIONARIO
# # print(fruit)
# print(fruit["tomato"])
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     print(description)
#     # if dict_key in fruit:
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("We doest have " + dict_key)
# for snack in fruit:
#     print(fruit[snack])
# orderd_key = list(fruit.keys())
# orderd_key.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])
# for f in sorted(fruit.keys()):
# for f in fruit:
#     print(f + " - " + fruit[f])
# for val in fruit.values():
#     print(val)
# print('-' * 40)
# for key in fruit:
#     print(fruit[key])
#
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)
print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))
