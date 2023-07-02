import mysql.connector
from tabulate import tabulate
conn = mysql.connector.connect(host='localhost',password ='root', user='root',database ='customer_details')

if conn.is_connected():
    print("connection established") 


def insert():
    id = input("Enter Id:")
    name = input("Enter Name:")
    age = input("Enter Age:")
    address = input("Enter Address:")
    contact = input("Enter Contact:")

    res = conn.cursor()
    sql = "insert into datas(id,name,age,address,contact) values(%s,%s,%s,%s,%s)"
    res.execute(sql,(id,name,age,address,contact))
    conn.commit()
    print("\n")
    print("Record Insert Succcessfully")

def select():
    res = conn.cursor()
    sql = "select * from datas"
    res.execute(sql)
    result = res.fetchall()
    #result = res.fetchone()
    #result = res.fetchmany(2)
    print("\n")
    print(result)
    #print(tabulate(result, headers =["Id","Name","Age","Address","Contact"]))

def update():
    print("1.Id")
    print("2.Name")
    print("3.Age")
    print("4.Address")
    print("5.Contact")
    option = int(input("\nwhich field you want to update?:"))
    if option == 1:
        id = input("Enter your id:")
        name = input("Enter your name:")
        cur = conn.cursor()
        sql = "update dates set name = %s where id =%s"
        cur.execute(sql,(name,id))
        conn.commit()
        select()
        print("\n")
        print("update successfully")
    elif option == 2:
        id = input("Enter your id:")
        age = input("Enter your age:")
        cur = conn.cursor()
        sql = "update dates set age = %s where id =%s"
        cur.execute(sql,(age,id))
        conn.commit()
        select()
        print("\n")
        print("update successfully")
    elif option == 3:
        id = input("Enter your id:")
        address = input("Enter your address:")
        cur = conn.cursor()
        sql = "update dates set address = %s where id =%s"
        cur.execute(sql,(address,id))
        conn.commit()
        select()
        print("\n")
        print("update successfully")

    elif option == 4:
        id = input("Enter your id:")
        contact = input("Enter your contact:")
        cur = conn.cursor()
        sql = "update dates set contact = %s where id =%s"
        cur.execute(sql,(contact,id))
        conn.commit()
        select()
        print("\n")
        print("update successfully")

def delete():
    id = input("Enter your id:")
    res = conn.cursor()
    sql = "delete from datas where id = %s"
    res.execute(sql,(id,))
    conn.commit()
    print("\n")
    print("Record Deleted Successfully...!!!")

while True:
    print("1.Insert Record")
    print("2.Select Record")
    print("3.Update Record")
    print("4.Delete Record")
    print("5.Exit")
    print("\n")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        insert()
    elif choice == 2:
        select()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        quit()
    else:
        print("Invalid Option..!!!")
    
