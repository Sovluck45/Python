text = open("text_3.txt", "r")
calc = text.read().split("\n")
poor = []
salary = []
for i in calc:
    if i == float and float(i) < 20000:
        poor.append(i)
    salary.append(i)
print(f'Оклад меньше 20.000 {poor}, '
      f'средний оклад {sum(map(float, salary)) / len(salary)}')
# не знаю как решить эту задачу
