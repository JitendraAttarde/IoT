from dbutils.execute import execute_query
from dbutils.execute import execute_select_query

def insert_value(type, location, value):
    # type, location, value
    query = f"insert into sensorsLog(type, location, value) values('{type}', '{location}', {value});"

    execute_query(query)

    print(f"{type} Sensor's Value is inserted into table successfully")

# insert_value("LM35", "Nira", 32)

def get_temperatures():
    query = f"select * from sensorsLog where type = 'LM35';"

    temps = execute_select_query(query)

    # print(temps)
    for temp in temps:
        print(f"location = {temp[2]}, temp = {temp[3]}, time = {temp[4]}")

get_temperatures()

def get_intensity():
    query = f"select * from sensorsLog where type = 'LDR';"

    intensities = execute_select_query(query)

    # print(intensities)
    for i in intensities:
        print(f"location = {i[2]}, intensity = {i[3]}, time = {i[4]}")

get_intensity()
