

import sqlite3
import random
import string


#connect & cursor 
conn = sqlite3.connect("friends.db")
cursor = conn.cursor()


#Add new column (run once)
cursor.execute("ALTER TABLE Friends ADD COLUMN missing_field TEXT")

#Put one random character in the new column

random_char = random.choice(string.ascii_letters)
cursor.execute(
    "UPDATE Friends SET missing_field = ?",
    (random_char,)
)

# View table (SQL viewer)
cursor.execute("SELECT * FROM Friends")
rows = cursor.fetchall()


print("Friends table:")
for row in rows:
    print(row)


conn.commit()
conn.close()


