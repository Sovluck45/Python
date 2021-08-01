n = input("Введите число: ")
while n < "0":
    print("Число должно быть больше 0!")
    n = int(input("Введите число заново: "))
print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")
