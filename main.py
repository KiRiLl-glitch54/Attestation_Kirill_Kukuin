import datetime


def display_menu():
    print("\n--- Book Management App ---")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")
    print("-------------------------")

def add_new_book():
    print("\n--- Добавить книгу ---")
    author = input("Автор: ")
    title = input("Название: ")
    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if not (1 <= rating <= 5):
                raise ValueError
            break
        except ValueError:
            print("Неверная оценка. Введите число от 1 до 5.")
    read_date = input("Дата прочтения (ГГГГ-MM-ДД, оставьте пустым для сегодняшней даты): ")
    if not read_date:
        read_date = datetime.date.today().isoformat()
    
    try:
        new_book = Book(author, title, rating, read_date)
        add_book(new_book)
    except ValueError as e:
        print(f"Ошибка при добавлении книги: {e}")

def show_all_books():
    """Displays all books currently in storage."""
    print("\n--- Все книги ---")
    books = get_all_books()
    if not books:
        print("Библиотека пуста.")
        return
    for i, book in enumerate(books, 1):
        print(f"{i}. {book.title} by {book.author}, Rating: {book.rating}, Read: {book.read_date}")

def show_average_rating():
    """Displays the average rating of all books."""
    print("\n--- Средняя оценка ---")
    avg_rating = calculate_average_rating()
    if avg_rating == 0.0:
        print("Нет книг для подсчета средней оценки.")
    else:
        print(f"Средняя оценка всех книг: {avg_rating:.2f}")

def show_author_statistics():
    """Displays statistics for each author."""
    print("\n--- Статистика по авторам ---")
    stats = get_author_statistics()
    if not stats:
        print("Нет книг для статистики по авторам.")
        return
    for author, data in stats.items():
        print(f"Автор: {author}")
        print(f"  Всего книг: {data['total_books']}")
        print(f"  Средняя оценка: {data['average_rating']:.2f}")

def delete_book():
    """Prompts for a book title and removes it."""
    print("\n--- Удалить книгу ---")
    title_to_remove = input("Введите название книги для удаления: ")
    remove_book(title_to_remove)

def main():
    """Main function to run the application."""
    while True:
        display_menu()
        choice = input("Выберите опцию: ")

        if choice == '1':
            add_new_book()
        elif choice == '2':
            show_all_books()
        elif choice == '3':
            show_average_rating()
        elif choice == '4':
            show_author_statistics()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("Выход из приложения. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

main()
