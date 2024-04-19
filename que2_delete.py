import dbconn

def delete_person(Empid):
    # get connection
    conn = dbconn.get_connection()

    # form a query
    query = f"delete from employee where Empid = %s;"
    val = (Empid, )

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()



delete_person(4)












