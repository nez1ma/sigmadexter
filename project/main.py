from revision.hw_functions_utils import say_hello, find_max_number, multiply_numbers


def main():
    print(say_hello())

    print(find_max_number([1, 2, "x", 3.5, -10]))
    print(find_max_number([]))

    print(multiply_numbers(4, 5))
    print(multiply_numbers(2.5, 2))


if __name__ == "__main__":
    main()
