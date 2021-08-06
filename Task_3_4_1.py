def my_func(x, y):
    if x > 0 and y < 0:
        return x ** y
    else:
        print("Ошибка, значения введены неправильно!")
    return


print(my_func(
    x=float(input("Введите действительное положительное число: ")),
    y=int(input("Введите целое отрицательное число: "))))
