import sqlite3

conn_obj = sqlite3.connect('userData.db')
cursor_obj = conn_obj.cursor()


def func_clearData():
    cursor_obj.execute("DROP TABLE IF EXISTS data_user")
    table = """CREATE TABLE "data_user" ("userID" INTEGER NOT NULL, 
    "userName" TEXT NOT NULL, 
    "userPass" TEXT NOT NULL, 
    "userViolations" INTEGER, 
    PRIMARY KEY("userID"));"""
    cursor_obj.execute(table)
    print("Table data cleared")


def userCredCheck():
    while True:
        username = str(input("Enter your Username: "))
        password = str(input("Enter your Password: "))
        params = (username, password)
        cursor_obj.execute("SELECT * FROM data_user WHERE userName = ? AND userPass = ?", params)
        row = cursor_obj.fetchone()
        if row is not None:
            print("Correct Password")
            break


def updateViolation():
    while True:
        username = str(input("Enter the Username: "))
        violations = int(input("Enter the number of violations: "))
        cursor_obj.execute("SELECT * FROM data_user WHERE userName = ?", username)
        row = cursor_obj.fetchone()
        params2 = (violations, username)
        if row is not None:
            cursor_obj.execute("UPDATE data_user SET userViolations = ? WHERE userName = ? AND userPass = ?", params2)
            break

