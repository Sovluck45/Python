from itertools import count
from math import factorial
number = int(input("Введите число для получения факториала: "))


def generator():
    for el in count(number):
        yield factorial(el)


g = generator()
n = number
for i in g:
    if n < number + 1:
        print(i)
        n += 1
    else:
        break
