from dbutils.execute import execute_select_query

def get_empinfo():
    query = "select * from employee;"

    return execute_select_query(query)