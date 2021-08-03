words = input("Введите слова: ")
w = words.split()
for ind, el in enumerate(w, 1):
    if len(el) >= 10:
        el = el[:10]
    print(f"{ind}, {el}")
