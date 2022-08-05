import sqlite3

conn_obj = sqlite3.connect('userData.db')
cursor_obj = conn_obj.cursor()


def func1():
    while True:
        username = str(input("Enter your Username: "))
        password = str(input("Enter your Password: "))
        violations = int(input("Enter the number of violations: "))
        params = (username, password)
        cursor_obj.execute("SELECT * FROM data_user WHERE userName = ? AND userPass = ?", params)
        row = cursor_obj.fetchone()
        params2 = (violations, username, password)
        if row is not None:
            cursor_obj.execute("UPDATE data_user SET userViolations = ? WHERE userName = ? AND userPass = ?", params2)
            break


func1()
print("Commits made successfully!")
