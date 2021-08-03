month = int(input("Введите номер месяца от 1 до 12: "))
winter = {"m_1": 'январь', "m_2": 'февраль', "m_12": 'декабрь'}
summer = {"m_6": 'июнь', "m_7": 'июль', "m_8": 'август'}
autumn = {"m_9": 'сентябрь', "m_10": 'октябрь', "m_11": 'ноябрь'}
spring = {"m_3": 'март', "m_4": 'апрель', "m_5": 'май'}
while month <= 0 or month > 12:
    month = int(input("Введите номер месяца от 1 до 12 заново: "))
if month == 1:
    print(str("Сейчас зима, месяц"), winter.get("m_1"))
elif month == 2:
    print(str("Сейчас зима, месяц"), winter.get("m_2"))
elif month == 3:
    print(str("Сейчас весна, месяц"), spring.get("m_3"))
elif month == 4:
    print(str("Сейчас весна, месяц"), spring.get("m_4"))
elif month == 5:
    print(str("Сейчас весна, месяц"), spring.get("m_5"))
elif month == 6:
    print(str("Сейчас лето, месяц"), summer.get("m_6"))
elif month == 7:
    print(str("Сейчас лето, месяц"), summer.get("m_7"))
elif month == 8:
    print(str("Сейчас лето, месяц"), summer.get("m_8"))
elif month == 9:
    print(str("Сейчас осень, месяц"), autumn.get("m_9"))
elif month == 10:
    print(str("Сейчас осень, месяц"), autumn.get("m_10"))
elif month == 11:
    print(str("Сейчас осень, месяц"), autumn.get("m_11"))
elif month == 12:
    print(str("Сейчас зима, месяц"), winter.get("m_12"))
# Длинный, не додумался как сделать короче
