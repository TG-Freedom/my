import poems
import sign

name = sign.SIGN_TEMPLATE.format(name="Pavel")

print(name)

# Побажання до курсу
wishes = "Хочу більше практичних завдань!\nХочу глибше розуміти бібліотеки Python!"
print(wishes)

# Лінія розділення
line = "*" * 74
print(line)


# Перший вірш
print(poems.POEM_ONE)

# Лінія розділення
print(line)

# Другий вірш
print(poems.POEM_TWO)

# Лінія розділення
print(line)
