# CRUD operacije nad podacima u bazi podataka
import sqlite3


DB_PATH = './data_store/baza.db'


try:
    with sqlite3.connect(DB_PATH) as conn:
        pass

except Exception as ex:
    print(f'Dogodila se greska {ex}.')
