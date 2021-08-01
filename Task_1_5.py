proceeds = int(input("Введите значение выручки: "))
cost = int(input("Введите значение издержки: "))
profit = proceeds - cost
if proceeds > cost:
    print("Выручка больше издержек")
elif cost > proceeds:
    print("Убыток больше выручки")

if proceeds > cost:
    profitability = profit / proceeds * 100
    print(f"Рентабельность составляет {profitability} %")
    number = int(input("Укажите численность сотрудников: "))
    prof_pers = profit / number
    print(f"Количество прибыли на одного человека составляет {prof_pers}")
