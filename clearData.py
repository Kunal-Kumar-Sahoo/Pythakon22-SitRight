import sqlite3

conn_obj = sqlite3.connect('userData.db')
cursor_obj = conn_obj.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS data_user")

table = """CREATE TABLE "data_user" ("userID" INTEGER NOT NULL, 
"userName" TEXT NOT NULL, 
"userPass" TEXT NOT NULL, 
"userViolations" INTEGER, 
PRIMARY KEY("userID"));"""

cursor_obj.execute(table)
print("Table data cleared")
