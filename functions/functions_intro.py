def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers
    :param x: First value that user passed
    :param y: Second value that user passed
    :return: The multiple from this two values
    """
    #result = x * y
    return x * y


def is_palindrome(string: str) -> bool:
    """
    Verify if a string is an palindrome
    :param string:
    :return: True in case it is a palindrome or false case not.
    """
    return string[::-1].casefold() == string.casefold()


def is_sentence_palindrome(sentence: str) -> bool:
    """
    Verify is a sentence is a palindrome.

    The function group words and ignore not alnumeric chars
    :param sentence:
    :return: Return True or False
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


# word = input("Please enter a word to check: ")
# if is_sentence_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

answer = multiply(18, 3)
print(answer)


p = is_sentence_palindrome(aaaa)