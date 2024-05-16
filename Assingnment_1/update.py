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

def update_person(uid, mobile):
    # get connection
    conn = get_connection()

    # form a query
    query = f"update persons SET mobile = %s where uid = %s;"
    val = (mobile, uid)

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()



update_person(45, "77498558")













