# my_list = ["a", "b", "c", "d"]
# letters = "hauhauahaua"
# numbers = "123456789"
# new_string = ",".join(my_list)
# new_string = ",".join(letters)
# new_string = " mississippi ".join(numbers)

locations = {0: "you are sitting in front of a computer learning python",
             1: "You are standing at the end of the road before a small brick building",
             2: "You are at the top of the hill",
             3: "you are inside a building, a wel house for a small stream",
             4: "you are in a valley beside a stream",
             5: "you are in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are: " + available_exits).upper()
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
