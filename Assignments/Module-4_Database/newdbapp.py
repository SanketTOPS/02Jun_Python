import sqlite3

try:
    db=sqlite3.connect("tops.db")
    print("Database connected/created!")
except Exception as e:
    print(e)

#Table Create

tbl_create="create table studinfo(id integer primary key autoincrement,name text, city text)"

try:
    db.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)


#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('nirav','surat'),('mitesh','baroda'),('mahesh','ahmedabad'),('ramesh','navsari')"

try:
    db.execute(insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""


#Update Data
"""update_data="update studinfo set name='pratik',city='jamnagar' where id=9"
try:
    db.execute(update_data)
    db.commit()
    print("Record Updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where id=10"
try:
    db.execute(delete_data)
    db.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)"""


cr=db.cursor()
#Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i)
except Exception as e:
    print(e)
    