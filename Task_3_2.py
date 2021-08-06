def profile(name, s_name, b_year, city, email, t_number):
    print(f"Имя - {name};"
          f" Фамилия - {s_name};"
          f" Год рождения - {b_year};"
          f" Город проживания - {city};"
          f" Электронная почта - {email};"
          f" Номер телефона - {t_number}")


profile(name=input("Введите имя: "),
        s_name=input("Введите фамилию: "),
        b_year=input("Введите год рождения: "),
        city=input("Введите город проживания: "),
        email=input("Введите свою электронную почту: "),
        t_number=input("Введите свой номер телефона: "))
