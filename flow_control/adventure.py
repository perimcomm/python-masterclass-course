adventure_exists = ["north", "east", "south", "west"]
chosen_exit = ""

while chosen_exit not in adventure_exists:
    chosen_exit = input("Please choose a direction:")
    if chosen_exit.lower() == "quit":
        print("Game over")
        break

print("aren't you glad you got out of there? ")