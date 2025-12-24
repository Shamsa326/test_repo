


# #(Schema) create tasks table:

# CREATE TABLE IF NOT EXISTS tasks (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT NOT NULL,
#     description TEXT,
#     status TEXT DEFAULT 'pending'
#     created_at DATETIME DEFAULT CURRENT_TIMESTAMP 
# )


#python Script to create sql3 db:

# Import library 
import sqlite3

#Connect to Sql3 db (creates file if it doesn't exist)
conn = sqlite3.connect("tasks.db")

#Create a cursor (transportation)
cursor=conn.cursor()

#Create tasks table (execute) copy Schema here

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP 
)"""
)

#Save changes and close connection

conn.commit()
conn.close()

print("Database and tasks table created")