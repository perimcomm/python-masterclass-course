shopping_list = ["leite", "macarrao", "eggs", "pao", "arroz", "spam", "feijao"]

item_to_find = "albratross"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print(found_at)
else:
    print("Not found")
