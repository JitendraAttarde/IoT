#import module of mysql connector
import mysql.connector

#create a connection with mysql database server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb",
)

#create a query
empid = int(input("Enter EmpID : "))
name = input("Enter Name : " )
department = input("Enter Department: ")
email = input("Enter Email ID : ")
salary = int(input("Enter Salary : "))
date_of_joining = str(input("Enter date of joining : ")) 

employees = f"insert into employees values({empid}, '{name}', '{department}', ''{email}', {salary}, '{date_of_joining}');"

#create the cursor to execute the query
cursor = connection.cursor()

#execute the query using cursor
cursor.execute(employees)

#after execution of query commit your changes
connection.commit()

#close the connection with mysql server
connection.close()
