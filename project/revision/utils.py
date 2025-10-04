from typing import List
import requests
import json
from datetime import datetime

SOURCE_TOKEN = "dUcpSF6YYLDjP7h3zDepDNip"
HOST = "https://s1523333.eu-nbg-2.betterstackdata.com"


def send_log(message: str):
    payload = {
        "dt": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "message": message
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SOURCE_TOKEN}"
    }
    try:
        r = requests.post(HOST, headers=headers, data=json.dumps(payload))
        if r.status_code not in (200, 202):
            print(f"Failed to send log, status code: {r.status_code}")
    except Exception as e:
        print("Failed to send log:", e)


def greet_person(name: str = "Гість") -> str:
    result = f"Привіт, {name}!"
    send_log(f"greet_person({name}) -> {result}")
    return result


def is_even(number: int) -> bool:
    result = number % 2 == 0
    send_log(f"is_even({number}) -> {result}")
    return result


def reverse_string(text: str) -> str:
    result = text[::-1]
    send_log(f"reverse_string({text}) -> {result}")
    return result


def calculate_average(numbers: List[float]) -> float:
    if not numbers:
        result = 0.0
    else:
        result = sum(numbers) / len(numbers)
    send_log(f"calculate_average({numbers}) -> {result}")
    return result


def add_person_to_list(people: List[str], person: str) -> List[str]:
    new_list = people.copy()
    new_list.append(person)
    send_log(f"add_person_to_list({people}, {person}) -> {new_list}")
    return new_list


def count_vowels(text: str) -> int:
    vowels = "aeiouаеєиіїоуюя"
    result = sum(1 for ch in text.lower() if ch in vowels)
    send_log(f"count_vowels({text}) -> {result}")
    return result


def fahrenheit_to_celsius(f: float) -> float:
    result = (f - 32) * 5.0 / 9.0
    send_log(f"fahrenheit_to_celsius({f}) -> {result}")
    return result