from typing import List, Union
import logging.handlers


logger = logging.getLogger("homework")
logger.setLevel(logging.INFO)

SOURCE_TOKEN = "Rhjrp1ogaSMzSt1RK93jhk4d"

http_handler = logging.handlers.HTTPHandler(
    host="in.logs.betterstack.com",
    url=f"/sources/{SOURCE_TOKEN}",
    method="POST",
)

if not logger.handlers:
    logger.addHandler(http_handler)



def say_hello() -> str:
    result = "Hello, buddy"
    logger.info(f"say_hello() called -> result: {result}")
    return result


def find_max_number(numbers: List[Union[int, float, str]]) -> Union[int, float]:
    filtered = [n for n in numbers if isinstance(n, (int, float))]
    result = max(filtered, default=0)
    logger.info(f"find_max_number({numbers}) -> {result}")
    return result


def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    result = a * b
    logger.info(f"multiply_numbers({a}, {b}) -> {result}")
    return result
