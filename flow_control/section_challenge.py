def options_to_be_chosed():
    print("1 - Learn python")
    print("2 - Learn Java")
    print("3 - Go Swimming")
    print("0 - quit")

choice = int(input("Please pick a number"))

while choice != 0:
    options_to_be_chosed()

    choice = int(input())
