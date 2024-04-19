# import mysql connector
import mysql.connector

# function to create a connection
def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "sunbeam",
        password = "sunbeam",
        database = "iotdb"
    )

def update_person(Empid, Salary):
    # get connection
    conn = get_connection()

    # form a query
    query = f"update employee SET Empid = %s where Salary = %s;"
    val = (Empid, Salary)

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()



update_person(8, 30000)












