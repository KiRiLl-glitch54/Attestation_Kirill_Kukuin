from typing import List, Dict
import collections


def calculate_average_rating() -> float:
    # Assuming get_all_books is available in the global scope after previous cell execution
    books = get_all_books()
    if not books:
        return 0.0
    total_rating = sum(book.rating for book in books)
    return total_rating / len(books)

def get_author_statistics() -> Dict[str, Dict[str, float]]:
    # Assuming get_all_books is available in the global scope after previous cell execution
    books = get_all_books()
    author_stats = collections.defaultdict(lambda: {'total_books': 0, 'total_rating': 0})

    for book in books:
        author_stats[book.author]['total_books'] += 1
        author_stats[book.author]['total_rating'] += book.rating

    result = {}
    for author, stats in author_stats.items():
        avg_rating = stats['total_rating'] / stats['total_books']
        result[author] = {
            'total_books': stats['total_books'],
            'average_rating': avg_rating
        }
    return result
