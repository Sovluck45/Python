def int_func():
    w = input("Введите предложение: ").title()
    return w


print(int_func())

# def int_func():
#     w = input("Введите предложение: ")
#     words = []
#     for letter in w:
#         for i in letter:
#             if 122 >= ord(i) >= 97:
#                 letter.capitalize()
#                 words.append(letter)
#             elif ord(i) == 32:
#                 continue
#             else:
#                 continue
#     return words
#
#
# print(int_func())
# здесь пытался сделать распознование кириллицы,
# но смесь из кириллицы и латинских букв не распознаёт и выводит только раздельно буквы
