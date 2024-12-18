name = input("Введите свое имя: ") + "\n\n"
# age = input("Введите свой возрост: ")


# name = "fsfsfsdf \t vfvvdfvvdfv \t\t"

# name = name.title() # Делает все слова с большой буквы
# name = name.strip() # Убирает пробелы
# name = name.strip('0123456789 ') # Удалем все ненужные символы
# name = name.lstrip() # очешаем только справа пробелы
# name = name.rstrip() # очешаем только с лева пробелы
# name = name.lower() # все буквы делает маленькими
# name = name.upper() # Все буквы делает большими

# name = name.title().strip().lower('0123456789 ') # Можно все сократить в одну строчку
name = name.replace('.', '!')  # Замена занков с на
name = name.capitalize()  # Заменяет только первую букву на большую остольное все будет маленькими

multiplication = '*' * 74
print(multiplication)

print(name)
