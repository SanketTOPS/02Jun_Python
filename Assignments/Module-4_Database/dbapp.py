import sqlite3

try:
    dbcon=sqlite3.connect("temp.db")
    print("Database connected!")
except Exception as e:
    print(e)

#Table Create
tbl_create="create table studinfo(id integer primary key autoincrement,name text, city text)"

try:
    dbcon.execute(tbl_create)
    print("Table Created!")
except Exception as e:
    print(e)
