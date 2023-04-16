"""
odd/even number checker
Author: Wolf Paulus (https://wolfpaulus.com)
"""


def is_odd(num: int) -> bool:
    """Return True if num is odd, False otherwise."""
    return num % 2 == 1


def is_odd_str(num: str) -> str:
    """Return a string indicating whether num is odd or even."""
    if num.isnumeric():
        return f"{num} is {'odd' if is_odd(int(num)) else 'even'}."
    else:
        return "Please enter a number."


def is_calvin_henggeler(name: str) -> str:

    if '+' in name:
        split_name = name.split('+')
        name = " ".join(split_name)

    lower_name = name.lower()
    accepted_name_froms = ["calvin", "calvin henggeler", "calvin+henggeler"]
    if lower_name in accepted_name_froms:
        return "Hello, Calvin!"
    else:
        return f"{name}, You are not Calvin"

