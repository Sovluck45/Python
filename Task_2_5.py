rating = int(input("Введите новый элемент рейтинга: "))
my_rating = [8, 4, 2, 2, 1]
while rating <= 0 or rating > 10:
    rating = int(input("Заново введите элемент рейтинга: "))
if rating == 1:
    my_rating.append(rating)
elif 2 <= rating < 4:
    my_rating.insert(2, rating)
elif 4 <= rating < 8:
    my_rating.insert(1, rating)
elif 8 <= rating:
    my_rating.insert(0, rating)
str_r = " ".join(map(str, my_rating))
print(str_r)
