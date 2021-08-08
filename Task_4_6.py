from itertools import count
from itertools import cycle

number = int(input("Введите стартовое число: "))
stop_number = int(input("Введите конечное число: "))
for el in count(number):
    if el > stop_number:
        break
    else:
        print(el)

word = input("Введите слово: ")
x = 0
for i in cycle(word):
    if x > 10:
        break
    else:
        print(i)
        x += 1
