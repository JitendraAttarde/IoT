# import mysql connector
import mysql.connector

# create connection with mysql server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

# form a qery
query = "select * from persons;"

# create a cursor to execute query
cursor = connection.cursor()

# execute query using cursor
cursor.execute(query)

# get data from cursor
records = cursor.fetchall()     #   returns list of tuples

print(records)

# close the cursor
cursor.close()

# close the connection
connection.close()