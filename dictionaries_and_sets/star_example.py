numbers = (0, 1, 2, 3, 3.2, 4, 5)


def test_star(*args):
    print(args)
    for x in args:
        if not type(x) is int:
            raise TypeError("Error argument type")
        print(x)

test_star(0, 1, 2, 3, 4, 5)

print()
test_star()
