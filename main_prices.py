from prices import PRICES
from phrases import PHRASES

# Делаем приведствие
print("Вітаємо у ресторані 'Дача'!")
clirnt_name = input("Як до вас можна звертатися? ")

clirnt_name = clirnt_name.title() # Делает все слова с большой буквы
clirnt_name = clirnt_name.strip() # Убирает пробелы
clirnt_name = clirnt_name.strip('0123456789 ') # Удалем все ненужные символы
clirnt_name = clirnt_name.lstrip() # очешаем только справа пробелы
clirnt_name = clirnt_name.rstrip() # очешаем только с лева пробелы


print(f"Раді вас бачити, {clirnt_name}!\n")


# Пропонуємо страви
order = {}
for dish, phrase in PHRASES.items():
    print(phrase)
    try:
        portions = int(input(f"Скільки порцій {dish} ви бажаєте замовити? (Введіть число): "))
        if portions > 0:
            order[dish] = portions
    except ValueError:
        print("Будь ласка, введіть коректне число.")

# Обчислення вартості замовлення
print("\nФормуємо ваше замовлення...\n")
total_cost = 0
for dish, portions in order.items():
    price_per_portion = PRICES[dish]
    dish_cost = price_per_portion * portions
    total_cost += dish_cost
    print(f"{dish}: {portions} порцій x {price_per_portion:.2f} грн = {dish_cost:.2f} грн")

# Знижка
discount = total_cost * 0.15
final_cost = total_cost - discount

# Роздруковуємо чек
print("\nЧЕК:")
print("*" * 50)
for dish, portions in order.items():
    price_per_portion = PRICES[dish]
    dish_cost = price_per_portion * portions
    print(f"{dish}: {portions} порцій x {price_per_portion:.2f} грн = {dish_cost:.2f} грн")
print("*" * 50)
print(f"Загальна вартість: {total_cost:.2f} грн")
print(f"Знижка (15%): {discount:.2f} грн")
print(f"До оплати: {final_cost:.2f} грн")
print("*" * 50)
print(f"Дякуємо за ваше замовлення, {clirnt_name}! Гарного дня!")

# Меню
# order = {}
