import sqlite3

def execute(query):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute(query) 
    return cur.fetchall()