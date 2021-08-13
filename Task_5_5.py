from random import randint
with open("text_5.txt", "w") as numbers:
    numbers.writelines(str(randint(10, 101)))
    numbers.writelines(str(" "))
    numbers.writelines(str(randint(10, 101)))
    numbers.writelines(str(" "))
    numbers.writelines(str(randint(10, 101)))
    numbers.writelines(str(" "))
    numbers.writelines(str(randint(10, 101)))
    numbers.writelines(str(" "))
    numbers.writelines(str(randint(10, 101)))
with open("text_5.txt", "r") as read:
    r = read.read()
    print(f"Полученные числа: {r}")
with open("text_5.txt", "r") as calc:
    num = calc.read().split(" ")
    int_list = [int(el) for el in num]
    summa = sum(int_list)
    print(f"Сумма введённых чисел: {summa}")
