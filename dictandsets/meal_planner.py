from contents import pantry, recipes

#display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

display_dict = {}

for index, value in enumerate(recipes, 1):
    display_dict[str(index)] = value

while True:
    #Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")