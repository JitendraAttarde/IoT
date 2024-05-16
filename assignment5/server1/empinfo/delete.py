from dbutils.execute import execute_query

def delete_empinfo(empid):
    query = f"delete from employee where empid = {empid};"

    execute_query(query)