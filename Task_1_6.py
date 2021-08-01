first_km = int(input("Введите первый км: "))
last_km = int(input("Введите последний км: "))
day = 1
while first_km < last_km:
    first_km = first_km + first_km * 0.1
    day += 1
print(f"На {day} день спортсмен достиг не менее {last_km} км")
