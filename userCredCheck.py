import sqlite3

conn_obj = sqlite3.connect('userData.db')
cursor_obj = conn_obj.cursor()


def func1():
    while True:
        username = str(input("Enter your Username: "))
        password = str(input("Enter your Password: "))
        params = (username, password)
        cursor_obj.execute("SELECT * FROM data_user WHERE userName = ? AND userPass = ?", params)
        row = cursor_obj.fetchone()
        if row is not None:
            print("Correct Password")
            break


func1()
