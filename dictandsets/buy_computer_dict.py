available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "headphone"
}

available_parts["7"] = "dvd"

del available_parts["5"]
print(available_parts.items())
current_choice = None

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[currente_choice]
        print("Adding".format(chosen_part))
    else:
        for key, value in available_parts.items:
            print(f"{key}: {value}")
        print("0: to finish")

    
    currente_choice = input("> ")