def my_calc():
    sum_n = 0
    while True:
        n = input("Введите числа или Q для завершения: ").upper().split()
        for i in range(len(n)):
            if n[i] == "Q":
                break
            else:
                sum_n += int(n[i])
        return print(f"Результат: {sum_n}")


my_calc()
# никак не могу сделать программу бесконечной
