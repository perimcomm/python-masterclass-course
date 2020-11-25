def func(p1, p2, *args, k, **kwargs):
    print("Positional-or-keyword:......{}, {}".format(p1, p2))
    print("var-or-positional (*args):......, {}".format(args))
    print("Keyword..............{}".format(k))
    print("var-keyword:................{}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)


def sum_numbers(*args): #SEMPRE EH NECESSARIO DESCOMPACTAR A TUPLA
    sum = 0
    for i in args:
        sum += i
    return sum


print(sum_numbers(1, 2, 3))