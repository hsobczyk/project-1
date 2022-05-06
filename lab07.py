def one(n: int) -> int:
    """
    Function that adds all the numbers from 1 to n
    :param n: Input number
    :return: The result of the added sequence
    """
    if n < 2:
        return n
    else:
        return n + one(n - 1)


def two(num: int, pow: int) -> int:
    """
    Function that takes the power of a number
    :param num: An integer
    :param pow: An integer as exponent
    :return: The result of num^pow
    """
    if pow < 2:
        return num
    else:
        return num * two(num, pow - 1)


def three(n: int) -> str:
    """
    Function that counts down in a single line string
    :param n: an integer
    :return: returns a string of numbers in descending order
    """
    numbers = ''
    if n > 1:
        numbers += str(n) + " "
        numbers += three(n - 1)
    else:
        numbers += str(n)

    return numbers

def main() -> None:
    print(one(1))       # 1
    print(one(2))       # 3
    print(one(3))       # 6
    print(one(4))       # 10

    print()
    print(two(2, 1))    # 2
    print(two(2, 2))    # 4
    print(two(2, 3))    # 8
    print(two(3, 4))    # 81

    print()
    three(5)            # 5 4 3 2 1
    print()
    three(10)           # 10 9 8 7 6 5 4 3 2 1


if __name__ == '__main__':
    main()
