import functools
import operator
import time
import math
#1
def ex1(numbers):
    return functools.reduce(operator.mul, numbers)
numbers = [1, 2, 3]
print(ex1(numbers))

#2
def ex2(text):
    return [sum(1 for c in text if c.isupper()), sum(1 for c in text if c.islower())]
s = input()
print(ex2(s))

#3
def ex3(text):
    return text == "".join(reversed(text))
print(ex3(s))

#4
def ex4(n, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(n)
n = 25100
delay_ms = 2123
result = ex4(n, delay_ms)
print(f"Square root of {n} after {delay_ms} milliseconds is {result}")

#5
def ex5(elements):
    return all(elements)

print(ex5((1, 0, 1, 1)))