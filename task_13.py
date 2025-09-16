year_ = 2025
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
year_100 = year_ + (100 - age)
message = (
    f"Здравствуйте, {name}!\n"
    f"Сейчас вам {age} лет.\n"
    f"Вам исполнится 100 лет в {year_100} году .")
print(message)