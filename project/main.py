from revision.utils import (
    greet_person,
    is_even,
    reverse_string,
    calculate_average,
    add_person_to_list,
    count_vowels,
    fahrenheit_to_celsius,
)

def main():
    print(greet_person())
    print(greet_person("Іван"))

    print(is_even(4))
    print(is_even(7))

    print(reverse_string("Python"))

    print(calculate_average([1, 2, 3, 4, 5]))
    print(calculate_average([]))

    people = ["Anna", "Oleh"]
    updated = add_person_to_list(people, "Marta")
    print("Original:", people)
    print("Updated:", updated)

    print(count_vowels("Привіт, World!"))

    print(fahrenheit_to_celsius(32))
    print(fahrenheit_to_celsius(212))

if __name__ == "__main__":
    main()

