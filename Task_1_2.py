time = int(input("Введите время в секундах:"))
hours = time // 3600 % 60
minutes = time // 60 % 60
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")
