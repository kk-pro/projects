import sqlite3

def connect():
    conn=sqlite3.connect("kkhh.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task text, description text, date integer, time integer)")
    conn.commit()
    conn.close()

def insert(task, description, date, time):
    conn=sqlite3.connect("kkhh.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO tasks VALUES (NULL,?,?,?,?)",(task, description, date, time))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("kkhh.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(task="", date="", time=""):
    conn=sqlite3.connect("kkhh.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE task=? OR date=? OR time=?", (task,date,time))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("kkhh.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    
def update(id, task, description, date, time):
    conn=sqlite3.connect("kkhh.db")
    cur=conn.cursor()
    cur.execute("UPDATE tasks SET task=?, description=?, date=?, time=? WHERE id=?",(task, description, date, time, id))
    conn.commit()
    conn.close()

connect()

