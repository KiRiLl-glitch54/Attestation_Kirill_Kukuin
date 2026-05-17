import json
from datetime import datetime


class Book:
    pass

    def to_dict(self) -> dict:
        pass

    @staticmethod
    def from_dict(data: dict):
        pass

    def __repr__(self) -> str:
        return f"Book(author='{self.author}', title='{self.title}', rating={self.rating}, read_date='{self.read_date}')"
