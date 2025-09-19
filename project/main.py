from revision.hw_functions_utils import (
    say_hello, find_max_number, multiply_numbers, get_ticket_price,
    is_number_bigger_than_given, add_salt_to_list, get_string_length_no_whitespaces, get_auto_distance
)
from revision.utils import (
    greet_person, is_even, reverse_string, calculate_average,
    add_person_to_list, count_vowels, fahrenheit_to_celsius
)


def main():
    print(say_hello())
    print(greet_person())
    print(greet_person("Іван"))
    print(is_even(4))
    print(is_even(7))
    print(reverse_string("Python"))

    print(find_max_number([1, 2, "x", 3.5, -10]))
    print(find_max_number([]))
    print(calculate_average([1, 2, 3, 4, 5]))
    print(calculate_average([]))

    print(multiply_numbers(4, 5))
    print(multiply_numbers(2.5, 2))

    people = ["Anna", "Oleh"]
    updated = add_person_to_list(people, "Marta")
    print("Original:", people)
    print("Updated:", updated)

    print(count_vowels("Привіт, World!"))
    print(fahrenheit_to_celsius(32))
    print(fahrenheit_to_celsius(212))

    print(get_ticket_price(4))
    print(get_ticket_price(10))
    print(get_ticket_price(30))
    print(get_ticket_price(65))


if __name__ == "__main__":
    main()


