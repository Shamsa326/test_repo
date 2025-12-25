

import sqlite3
import time 


DB_NAME="friends.db"

#create table

def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Friends (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """)
    conn.commit()
    conn.close()


# Insert a new friend

def insert_friend(name, age):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Friends (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    print(f"Inserted: {name}, {age}")


# View tables in database
def view_tables():
    conn=sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("\nTables in database:")
    for table in tables:
        print(table[0])
    conn.close()

# View contents of a table

def view_table_contents(table_name, message=""):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    print(f"\n{message}")
    for row in rows:
        print(row)
    conn.close()

# Update a friend's age by name
def update_friend_age_by_name(name, new_age):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Get the current age first
    cursor.execute("SELECT age FROM Friends WHERE name = ?", (name,))
    result = cursor.fetchone()
    if not result:
        print(f"\nFriend '{name}' not found!")
        conn.close()
        return None  # No friend found
    old_age = result[0]

    # Update age
    cursor.execute("UPDATE Friends SET age = ? WHERE name = ?", (new_age, name))
    conn.commit()
    conn.close()
    print(f"\nUpdated {name}'s age from {old_age} to {new_age}")
    return old_age  # Return old age for reverting

# -------------------------------
# Main script
# -------------------------------

def main():
    setup_database()

    # Show tables
    view_tables()

    # Show original data
    view_table_contents("Friends", "BEFORE UPDATE")

    # Ask user which friend to update
    friend_name = input("\nEnter the name of the friend to update: ")
    new_age = int(input(f"Enter the new age for {friend_name}: "))

    # Update the friend and get old age
    old_age = update_friend_age_by_name(friend_name, new_age)
    if old_age is None:
        return  # Exit if friend not found

    # Show updated data
    view_table_contents("Friends", "AFTER UPDATE")

    # Wait 15 seconds
    print("\nWaiting 15 seconds before reverting...")
    time.sleep(15)

    # Revert the age
    update_friend_age_by_name(friend_name, old_age)

    # Show reverted data
    view_table_contents("Friends", "AFTER REVERT")

if __name__ == "__main__":
    main()


