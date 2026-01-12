
import sqlite3
import random
import string

#create database file
db = sqlite3.connect("users.db")
cur = db.cursor()

#create table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  name TEXT,
  phone TEXT,
  user_key TEXT
)
""")

#random data for the table 

names = ["Shamsa", "Hana", "Saeed", "Theyab"]

def rand_phone():
    phone = "50"
    for _ in range(8):
        phone += random.choice("0123456789")
    return phone

def rand_key():
    key = ""
    for _ in range(10):
        key += random.choice(string.ascii_letters + string.digits)
    return key

def clear_table():
    cur.execute(
        "Delete from users "
    )

clear_table()

for i in range(1, 6):
    cur.execute(
        "INSERT INTO users (id, name, phone, user_key) VALUES (?, ?, ?, ?)",
        (i, names[i % len(names)], rand_phone(), rand_key())
    )

db.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

db.close()

