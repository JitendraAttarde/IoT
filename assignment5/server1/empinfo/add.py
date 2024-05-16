from dbutils.execute import execute_query

def insert_empinfo(empid,name,email,dept,mobile_no):
    query = f"insert into employee values({empid},'{name}','{email}','{dept}','{mobile_no}');"

    execute_query(query)