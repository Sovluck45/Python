month = int(input("Введите номер месяца: "))
seasons = ['зима', 'лето', 'осень', 'весна']
while month <= 0 or month > 12:
    month = int(input("Введите номер месяца заново: "))
if month == 1 or month == 2 or month == 12:
    seasons.remove('лето')
    seasons.remove('осень')
    seasons.remove('весна')
    str_s = "".join(seasons)
    print(f"Сейчас {str_s}")
elif month == 3 or month == 4 or month == 5:
    seasons.remove('лето')
    seasons.remove('осень')
    seasons.remove('зима')
    str_s = "".join(seasons)
    print(f"Сейчас {str_s}")
elif month == 6 or month == 7 or month == 8:
    seasons.remove('зима')
    seasons.remove('осень')
    seasons.remove('весна')
    str_s = "".join(seasons)
    print(f"Сейчас {str_s}")
elif month == 9 or month == 10 or month == 11:
    seasons.remove('лето')
    seasons.remove('зима')
    seasons.remove('весна')
    str_s = "".join(seasons)
    print(f"Сейчас {str_s}")
# Опять же код получился громоздкий, не придумал как сделать проще
