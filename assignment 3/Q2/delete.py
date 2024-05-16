import dbconn

def delete_employee(empid):
    #get connection
    conn = dbconn.get_connection()

    #form a query
    query = f"delete from employees where empid = %s;"
    val = (empid,)

    #create a cursor
cursor = conn.cursor()

#execute the query
cursor.execute (query, val)

#commit the changes
conn.commit()

#close cursor as well as connection
curser.close()
conn.close()



delete_employee(41)