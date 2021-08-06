def my_func(n_1, n_2, n_3):
    return n_1 + n_2 + n_3 - min(n_1, n_2, n_3)


print(my_func(
    n_1=int(input("Введите первое число: ")),
    n_2=int(input("Введите второе число: ")),
    n_3=int(input("Введите третье число: "))))
