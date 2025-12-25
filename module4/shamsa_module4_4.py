


#Import libraries 

#create sql3 db:

import sqlite3

# Create SQLite database and table
conn = sqlite3.connect("friends.db")
cursor= conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Friends (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

conn.commit()
conn.close()


DB_NAME = "friends.db"


# Function to view all tables
def view_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Get table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    conn.close()

# Function to view contents of a table
def view_table_contents(table_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    print(f"\nContents of table '{table_name}':")
    for row in rows:
        print(row)

    conn.close()

# Function to insert a row into Friends table
def insert_friend(name, age):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Friends (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    print(f"Inserted: {name}, {age}")


# View tables
view_tables()

# Insert sample data
insert_friend("Shasha", 29)
insert_friend("Hanoya", 29)

#View contents of the Friends table
view_table_contents("Friends")


