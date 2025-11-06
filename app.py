# CRUD operacije nad podacima u bazi podataka
import sqlite3


DB_PATH = './data_store/baza.db'

# Knjiga ima jednog autora
class Book:
    def __init__(self, title: str, author: Author, price: float, description: str = '', isbn: str = ''):
        self.title = title
        self.price = price
        self.author = author
        self.description = description
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
CREATE TABLE IF NOT EXITS author
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS book
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NULL,
    isbn TEXT NULL,
    price REAL NOT NULL,
    author_id INTEGER NOT NULL,

    FOREIGN KEY (author_id)
        REFERENCES author (id)
)
'''



try:
    with sqlite3.connect(DB_PATH) as conn:
        pass

except Exception as ex:
    print(f'Dogodila se greska {ex}.')
