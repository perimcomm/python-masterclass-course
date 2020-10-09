shopping_list = ["leite",
                 "macarrao",
                 "eggs",
                 "pao",
                 "arroz",
                 "spam",
                 "feijao"
                 ]

another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]

print(shopping_list)
print(id(shopping_list))

a = b = c = d = e = f = another_list
print(another_list)
print(a)
b.append("cream")
print(c)
print(d)