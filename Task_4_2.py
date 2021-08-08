n_list = [2412, 313, 5123, 2, 21, 6, 123, 62, 414, 0, 54, 7]
new_list = [el for el in n_list if el > n_list[n_list.index(el)-1]]
new_list.pop(0)
print(f"Старый список: {n_list}")
print(f"Новый список: {new_list}")
