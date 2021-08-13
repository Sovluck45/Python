dict_s = {}
with open("text_6.txt", "r") as school:
    for line in school:
        data = line.replace("(", " ").split()
        dict_s[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
    print(dict_s)
