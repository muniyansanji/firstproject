import mysql.connector
con=mysql.connector.connect(host ="localhost",user = "root",password="root",database="muniyan")
if con:
    print("connected")
else:
    print("connection error")