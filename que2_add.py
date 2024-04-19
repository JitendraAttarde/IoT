#import module of mysql connector
import mysql.connector

# create a connection with mysql database server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

# create a query
Empid = int(input("Enter Empid : "))
Name = input("Enter Name : ")
Department = input("Enter Department : ")
Email = input("Enter Email :")
Salary = int(input("Enter Salary : "))
Date_of_joining = input("Enter Date_of_joining : ")

query = f"insert into employee values({Empid}, '{Name}', '{Department}', '{Email}', {Salary},'{Date_of_joining}');"

# create a cursor to execute the query
cursor = connection.cursor()

# execute query using cursor
cursor.execute(query)

# after execution of query commit your changes
connection.commit()

# close the cursor
cursor.close()

#close the connection with mysql server 
connection.close()
