from dbutils.execute import execute_query

def update_empinfo(choice,nvalue,empid):
    if choice == 'email':
        query = f"update empinfo SET email='{nvalue}' where empid = {empid};"
    elif choice == 'moblie_no':
        query = f"update empinfo SET mobile='{nvalue}' where empid = {empid};"
    elif choice == 'dept':
        query = f"update empinfo SET dept='{nvalue}' where empid = {empid};"    

    execute_query(query)        