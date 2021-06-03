import sqlite3

def create_db():
    connection = sqlite3.connect('UserInfo.db')
    c = connection.cursor()
    c.execute("""CREATE TABLE userDetails(
    highScore text
    )""")
    connection.commit()
    connection.close()

def show():
    con = sqlite3.connect('UserInfo.db')
    c = con.cursor()
    c.execute("SELECT *, oid FROM userDetails")
    data = c.fetchall()
    con.commit()
    con.close()
    return data

def add(un):
    con = sqlite3.connect('UserInfo.db')
    c = con.cursor()
    c.execute("INSERT INTO userDetails VALUES(:name)",{
        'name': un
    })
    con.commit()
    con.close()

def clear():
    con = sqlite3.connect('UserInfo.db')
    c = con.cursor()
    for i in range(4):
        c.execute(f"DELETE FROM userDetails WHERE oid = {i}")
    con.commit()
    con.close()

