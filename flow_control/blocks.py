name = input("Please enter your name: ")
age = int(input("How old are you: {0}? ".format(name)))

if age < 18:
    print("You cannot drive drive")
    print("Please put an X in the box")
elif age == 900:
    print("Sorry, Yoda, you die in return of the jedi")
else:
    print("You can drive")
