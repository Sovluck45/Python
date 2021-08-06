def calc_func(n_1, n_2):
    try:
        return n_1 / n_2
    except ZeroDivisionError:
        return print("Ошибка!")


print(f"Результат вычислений: ", calc_func(n_1=float(input("Введите первое число: ")),
                                           n_2=float(input("Введите второе число: "))))
