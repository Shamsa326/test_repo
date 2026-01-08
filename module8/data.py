
import sqlite3


# create database :

db = sqlite3.connect("data.db")
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS data (
    id INTEGER,
    name TEXT
)
""")
cursor.execute("INSERT INTO data VALUES (1, 'Shamsa')")
cursor.execute("INSERT INTO data VALUES (2, 'Hana')")
cursor.execute("INSERT INTO data VALUES (3, 'Theyab')")
db.commit()
db.close()



