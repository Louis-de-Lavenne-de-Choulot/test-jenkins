import sqlite3
from flask import app
import flask
import jsonify

def get_db_connection():
    # Connect to the database
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/data')
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)
def init_db():
    conn = get_db_connection()
    # item table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
            )''')
    conn.commit()
    conn.close()
if __name__ == '__main__':
    # init db 
    init_db()
    app.run(host='0.0.0.0', port=3000)
