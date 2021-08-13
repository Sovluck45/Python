my_file = open("Lesson_5.txt", "x")
while True:
    my_str = str(input("Введите данные: "))
    if my_str == "":
        break
    else:
        my_file = open("Lesson_5.txt", "a")
        my_file.write(f"{my_str}\n")
my_file.close()
