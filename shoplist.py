print("Здравствуйте! Вас приветствует продуктовый ассистент. Ниже указаны пункты меню: ")
print("1. Добавить товар")
print("2. Удалить товар")
print("3. Показать список")
print("4. Выход")

shop_list = []

while True:
    choice = int(input("Выберите действие: "))

    if choice == 1:
        item = input("Напишите, какой товар вы хотите внести в список: ")
        shop_list.append(item)
    
    if choice == 2:
        item = input("Напишите, какой товар вы хотите удалить из списка: ")

        if item in shop_list:
            shop_list.remove(item)
            print("Товар успешно удалён")
        else:
            print("Указанного товара нет в списке")

    if choice == 3:
        print("Вот ваш список покупок: ")
        # for item in shop_list:
        #     print(item)

        print(",".join(shop_list))

    if choice == 4:
        break



# 120 10 14 32 320
# 120 + 10 + 14 + 32 + 320 = 496
# 496 / 5 = 99.2