import json
from typing import List, Optional


FILE_PATH = 'books.json'

def _load_books() -> List[Book]:
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Book.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Предупреждение: {FILE_PATH} пуст или содержи невалидный JSON. Начинаю с пустого листа.")
        return []

def _save_books(books: List[Book]):
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump([book.to_dict() for book in books], f, ensure_ascii=False, indent=4)

def add_book(book: Book):
    books = _load_books()
    books.append(book)
    _save_books(books)
    print(f"Книга под названием '{book.title}' под авторством {book.author} добавлена.")

def get_all_books() -> List[Book]:
    return _load_books()

def remove_book(title: str) -> bool:
    books = _load_books()
    initial_len = len(books)
    books = [book for book in books if book.title.lower() != title.lower()]
    if len(books) < initial_len:
        _save_books(books)
        print(f"Книга под названием '{title}' была удалена.")
        return True
    print(f"Книга под названием '{title}' не найдена.")
    return False

def find_books_by_author(author: str) -> List[Book]:
    books = _load_books()
    return [book for book in books if book.author.lower() == author.lower()]
