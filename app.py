# CRUD operacije nad podacima u bazi podataka
import sqlite3


DB_PATH = './data_store/baza.db'

# Knjiga ima jednog autora
class Book:
    def __init__(self, title: str, author: Author, description: str, price: float, isbn: str = ''):
        self.title = title
        self.author = author
        self.description = description
        self.price = price
        self.isbn = isbn

    def __str__(self):
        return f'{self.title} ({self.author.full_name})'

# Autor ima vise knjiga
class Author:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self._full_name()
        self.books = []

    def _full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    def add_book(self, book: Book):
        self.books.append(book)


sql_create_tables = '''

'''


try:
    with sqlite3.connect(DB_PATH) as conn:
        pass

except Exception as ex:
    print(f'Dogodila se greska {ex}.')
