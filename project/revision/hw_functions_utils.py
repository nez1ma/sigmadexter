from typing import List, Union
import requests
import json
import uuid

SOURCE_TOKEN = "dUcpSF6YYLDjP7h3zDepDNip"
BASE_URL = "https://s1523333.eu-nbg-2.betterstackdata.com"

def send_log(message: str) -> None:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SOURCE_TOKEN}"
    }
    payload = {"message": message}
    try:
        r = requests.post(BASE_URL, headers=headers, data=json.dumps(payload))
        if r.status_code not in (200, 202):
            print(f"Failed to send log, status code: {r.status_code}")
    except Exception as e:
        print(f"Error sending log: {e}")


def say_hello() -> str:
    result = "Hello, buddy"
    send_log(f"say_hello() -> {result}")
    return result


def find_max_number(numbers: List[Union[int, float, str]]) -> Union[int, float]:
    filtered = [n for n in numbers if isinstance(n, (int, float))]
    result = max(filtered, default=0)
    send_log(f"find_max_number({numbers}) -> {result}")
    return result


def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    result = a * b
    send_log(f"multiply_numbers({a}, {b}) -> {result}")
    return result


def is_number_bigger_than_given(candidate_number: float, threshold: float) -> bool:
    result = candidate_number > threshold
    send_log(f"is_number_bigger_than_given({candidate_number}, {threshold}) -> {result}")
    return result


def add_salt_to_list(given_list: List[str]) -> None:
    identifier = uuid.uuid4().hex
    given_list.append(identifier)
    send_log(f"add_salt_to_list() -> appended {identifier}, list now: {given_list}")


def get_string_length_no_whitespaces(string: str) -> int:
    string_no_spaces = string.replace(" ", "")
    result = len(string_no_spaces)
    send_log(f"get_string_length_no_whitespaces('{string}') -> {result}")
    return result


def get_auto_distance(speed: float, time: float) -> float:
    result = speed * time
    send_log(f"get_auto_distance({speed}, {time}) -> {result}")
    return result
