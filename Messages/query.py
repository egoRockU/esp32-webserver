import sqlite3

conn = sqlite3.connect('./db/database.db')

if (conn):
    print("Connected to Database successfully")

# conn.execute('''CREATE TABLE Messages (
#              id INTEGER PRIMARY KEY,
#              message TEXT,
#              date datetime DEFAULT current_timestamp
#              )''')

conn.execute("DELETE FROM Messages")
conn.commit()