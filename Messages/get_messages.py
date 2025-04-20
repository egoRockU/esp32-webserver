import sqlite3

DATABASE = './db/database.db'

try:
    conn = sqlite3.connect(DATABASE)
    with conn:
        conn.row_factory = sqlite3.Row
        curs = conn.cursor()
        curs.execute("SELECT * FROM Messages")
        rows = curs.fetchall()

        for row in rows:
            print('date:', row['date'], '| message:', row['message'])
            
except sqlite3.Error as e:
    print(f"Database error: {e}")
