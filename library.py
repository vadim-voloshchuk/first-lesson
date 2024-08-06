print("Здравствуйте! Вас приветствует библиотека. Ниже указаны пункты меню: ")
print("1. Добавить книгу")
print("2. Удалить книгу")
print("3. Показать список книг")
print("4. Найти книгу")
print("5. Статистика по жанрам")

print("6. Выход")

library  = {}

while True:
    choice = int(input("Выберите действие: "))

    if choice == 1:
        book_title = input("Напишите название книги, которую вы хотите добавить в библиотеку: ")
        book_author = input("Напишите её автора: ")
        book_year = input("Напишите её год: ")
        book_genre = input("Напишите её жанр: ")

        if book_title in library:
            print("Такая книга уже есть в библиотеке")
        else:
            library[book_title] = {"автор": book_author, "год": book_year, "жанр": book_genre}

    
    # if choice == 2:
        # item = input("Напишите, какой товар вы хотите удалить из списка: ")

        # if item in shop_list:
        #     shop_list.remove(item)
        #     print("Товар успешно удалён")
        # else:
        #     print("Указанного товара нет в списке")
        

    if choice == 3:
        print("Вот список книг: ")
        for item in library:
            print(item)
            
    if choice == 5:
        genre_count = {}
        for info in library.values():
            genre = info['жанр']
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1
        print("Статистика по жанрам:")
        for genre, count in genre_count.items():
            print(f"- {genre}: {count} книг")


    if choice == 6:
        break