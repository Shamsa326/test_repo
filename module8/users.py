

import sqlite3


# create database :

db = sqlite3.connect("users.db")
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    name TEXT,
    age INTEGER
)
""")
cursor.execute("INSERT INTO data VALUES (1, 'Shamsa', '15')")
cursor.execute("INSERT INTO data VALUES (2, 'Hana','16')")
cursor.execute("INSERT INTO data VALUES (3, 'Theyab','3')")
db.commit()
db.close()


