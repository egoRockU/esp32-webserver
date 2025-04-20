from flask import Flask, g, request
import json
import sqlite3
from flask_cors import cross_origin

app = Flask(__name__)

DATABASE = './db/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def hello():
    return 'Hello'

@app.route('/message', methods = ['POST'])
@cross_origin()
def message():
    message = json.loads(request.data)['message']
    try:
        with sqlite3.connect(DATABASE) as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO Messages (message) VALUES (?)', (message,))
            conn.commit()
            print("Message has been successfully saved")
    except:
        conn.rollback()
        print("Error saving message")
    finally:
        conn.close()
    
    return "OK", 200


if __name__ == '__main__':
    app.run()