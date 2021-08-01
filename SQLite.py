import sqlite3
db = sqlite3.connect(':memory:')
db = sqlite3.connect('C:/SQLite/test.db')
db.close()
