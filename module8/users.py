import sqlite3

# creates DB
# conn=sqlite3.connect("users.db")
# cursor=conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         phone TEXT
#                )
#                """)

# conn.commit()

# # ask user for input
# name=input("Enter your name:").strip()
# phone=input("Enter your phone:").strip()
# # save to database
# cursor.execute("INSERT INTO users (name,phone) VALUES (?,?)",(name,phone))
# conn.commit()

# cursor.execute("SELECT * FROM users")
# rows= cursor.fetchall()
# for row in rows:
#     print(row)

# conn.close()


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

# ask user for input
# name=input("Enter your name:").strip()
# phone=input("Enter your phone:").strip()
# save to database
    cursor.execute("INSERT INTO users (name,phone) VALUES (?,?)",(name,phone))
    conn.commit()

    cursor.execute("SELECT * FROM users")
    rows= cursor.fetchall()
    # for row in rows:
    #     print(row)
    return rows

def list_user_info():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows= cursor.fetchall()
    # for row in rows:
    #     print(row)
    return rows

if __name__ == "__main__":
    # mcp.run(host="0.0.0.0", port=9000)
    # mcp.run()
    save_user_info("test01", "12345")