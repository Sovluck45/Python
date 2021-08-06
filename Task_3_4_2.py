def my_func(x, y):
    z = 1
    if x > 0 and y < 0:
        for i in range(abs(y)):
            z *= x
        if y >= 0:
            return
        else:
            return 1 / z
    else:
        return print("Ошибка, значения введены неправильно!")


print(my_func(float(input("Введите действительное положительное число: ")),
              int(input("Введите целое отрицательное число: "))))
