from sys import argv

try:
    script_name, hours, rate_per_h, prem = argv
    result = (int(hours) * int(rate_per_h)) + int(prem)
    print("Имя скрипта: ", script_name)
    print("Заработная плата: ", result)
except ValueError:
    print("Неправильно введены значения!")
