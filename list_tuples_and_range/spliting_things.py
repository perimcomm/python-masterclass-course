import logging

panagram = """The quick brown 
fox jumps\tover 
the lazy dog"""

words = panagram.split(sep=",")
print(words)

numbers = "9,22,372,036,854"
print(numbers.split(sep=","))

# values = "".join(char if char not in separators else " " for char in numbers).split())

list_of_strings = ["2", "4", "8", "12", "14", "16", "18", "20"]


def convert_string_list_to_integer(lista):
    list_of_integers = []
    for i in lista:
        list_of_integers.append(int(i))

    return list_of_integers

print(convert_string_list_to_integer(list_of_strings))
