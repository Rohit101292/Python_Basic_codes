import mysql.connector

db= mysql.connector.connect(host = "localhost", user = "root", password = "", database = "sql_store")
cursor = db.cursor()

sql_cmd ="select * from customers;"

dict ={}
cursor.execute(sql_cmd)
for i in cursor:
    print(i)

print(dict)