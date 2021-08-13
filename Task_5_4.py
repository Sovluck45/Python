translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus = []
with open('text_4.txt', 'r') as eng:
    for i in eng:
        i = i.split(" ", 1)
        rus.append(translate[i[0]] + " " + i[1])
    print(rus)
with open('text_4_new.txt', 'w') as rus_v:
    rus_v.writelines(rus)
