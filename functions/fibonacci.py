def calculate_fibonacci(n: int) -> int:
    """
    This function return `N` th number in the fibonacci sequence
    :param n:
    :return:
    """
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None

    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, calculate_fibonacci(i))

p = calculate_fibonacci()
