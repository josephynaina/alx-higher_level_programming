#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number1 = number
if number < 0:
    number1 = -number
x = number1 % 10
if x > 5:
    print(f"Last digit of {number} is {x} and is greater than 5")
elif x < 6:
    print(f"Last digit of {number} is {x} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {x} and is 0")

