import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
 Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));
"""

cursor.execute(table_info)
cursor.execute(''' INSERT Into STUDENT values("Chetan","AI AND ML","C") ''')
cursor.execute(''' INSERT Into STUDENT values("Caran","DL","B") ''')
cursor.execute(''' INSERT Into STUDENT values("Rahul","JAVA","A") ''')
cursor.execute(''' INSERT Into STUDENT values("Kruthik","DL","P") ''')
cursor.execute(''' INSERT Into STUDENT values("Chintu","DL","O") ''')

for row in cursor.execute(''' Select * from STUDENT'''):
    print(row)

connection.commit()
connection.close()

