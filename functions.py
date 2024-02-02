"""DESCRIPTION OF THE MODULE GOES HERE

Author: Aidan Smith
Class: CSI 160
Assignment: Week 3: Lab
Due Date: 2/4/2024

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
import string
from random import randint
import random


def random_number(low, high):
    return randint(low, high)


def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choices(letters, k=length))


def random_email(length):
    letters = string.ascii_lowercase
    digits = string.digits
    symbols = "_-"

    username = ''.join(random.choices(letters + digits, k=length))
    domain = random.choice(['gmail', 'yahoo', 'aol', 'hotmail', 'icloud'])
    extension = random.choice(['com', 'net', 'org'])

    return f"{username}@{domain}.{extension}"


num_result = random_number(1, 10)
print(num_result)

string_result = random_string(num_result)
print(string_result)

result = random_email(num_result)
print(result)
