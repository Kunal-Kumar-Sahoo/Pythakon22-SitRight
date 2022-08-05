import sqlite3

conn_obj = sqlite3.connect('userData.db')
cursor_obj = conn_obj.cursor()


def func_clearData() -> None:
    cursor_obj.execute("DROP TABLE IF EXISTS data_user")
    table = """CREATE TABLE "data_user" ("userID" INTEGER NOT NULL, 
    "userName" TEXT NOT NULL, 
    "userPass" TEXT NOT NULL, 
    "userViolations" INTEGER, 
    PRIMARY KEY("userID"));"""
    cursor_obj.execute(table)
    print("Table data cleared")


def getEmailId(username: str, password: str):
    pass



def userCredCheck(username: str, password: str) -> bool:
    # while True:
    # remaining body was initially inside the while loop
    params = (username, password)
    cursor_obj.execute("SELECT * FROM data_user WHERE userName = ? AND userPass = ?", params)
    row = cursor_obj.fetchone()
    if row is not None:
        print("Correct Password")
        return True
    else:
        print("User is non existing or you have entered wrong username/password")
        return False


def updateViolation(username: str, password: str, number_of_violations: int = 1) -> None:
    while True:
        # username = str(input("Enter the Username: "))
        cursor_obj.execute("SELECT userViolations FROM data_user WHERE userName = ?", username)
        row = cursor_obj.fetchone()
        value1 = row[0]
        violations1 = value1 + number_of_violations
        if row is not None:
            # violations = int(input("Enter the number of violations: "))
            # params2 = (violations, username)
            params2 = (violations1, username, password)
            cursor_obj.execute("UPDATE data_user SET userViolations = ? WHERE userName = ? AND userPass = ?", params2)
            break

