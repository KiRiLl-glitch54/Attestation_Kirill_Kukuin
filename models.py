import json
from datetime import datetime

class Book:
    def __init__(self, author: str, title: str, rating: int, read_date: str):
        if not (1 <= rating <= 5):
            raise ValueError("Рейтинг должен быть числом от 1 до 5 (включительно).")
        self.author = author
        self.title = title
        self.rating = rating
        # Store date as string for simplicity with JSON, assume ISO format for input
        self.read_date = read_date

    def to_dict(self) -> dict:
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "read_date": self.read_date
        }

    @staticmethod
    def from_dict(data: dict):
        return Book(
            author=data["author"],
            title=data["title"],
            rating=data["rating"],
            read_date=data["read_date"]
        )

    def __repr__(self) -> str:
        return f"Книга(author='{self.author}', title='{self.title}', rating={self.rating}, read_date='{self.read_date}')"
