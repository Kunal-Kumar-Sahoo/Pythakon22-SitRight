import sqlite3


def create_table():
    conn_obj = sqlite3.connect('userData.db')
    cursor_obj = conn_obj.cursor()

    table = """CREATE TABLE IF NOT EXISTS "data_user" ("userID" INTEGER NOT NULL, 
    "userName" TEXT NOT NULL, 
    "userPass" TEXT NOT NULL, "
    userViolations" INTEGER, 
    PRIMARY KEY("userID"));"""

    cursor_obj.execute(table)
    print("Table created")


def add_user():
    conn_obj = sqlite3.connect('userData.db')
    cursor_obj = conn_obj.cursor()
    a1 = int(input("Enter userID: "))
    b1 = str(input("Enter userName: "))
    c1 = str(input("Enter userPass"))

    params = (a1, b1, c1, 0)

    cursor_obj.execute("INSERT INTO data_user VALUES (?,?,?,?);", params)
    conn_obj.commit()
    print("Data entered successfully")


if __name__ == "__main__":
    create_table()
    add_user()
