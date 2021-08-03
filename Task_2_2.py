numbers = [input("Введите числа: ").split()]
for n in numbers:
    n[::2], n[1::2] = n[1::2], n[::2]
print(' '.join([str(n) for n in numbers]))
# не могу понять как сделать с нечётным количеством чисел
