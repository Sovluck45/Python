number = int(input("Введите целое число: "))
star_num = number
biggest_num = 0
while number > 0:
    digit = number % 10
    if digit > biggest_num:
        biggest_num = digit
        if biggest_num == 9:
            break
    number = number // 10
print(f"Наибольшая цифра в чиле {star_num} равна {biggest_num}")
