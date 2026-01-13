import sqlite3

def save_user_info(name, phone):
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT
                )
                """)

    conn.commit()

# save to database
    cursor.execute("INSERT INTO users (name,phone) VALUES (?,?)",(name,phone))
    conn.commit()

    cursor.execute("SELECT * FROM users")
    rows= cursor.fetchall()
    return rows

def list_user_info():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows= cursor.fetchall()
    return rows

if __name__ == "__main__":
    save_user_info("test01", "12345")