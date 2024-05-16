from flask import Flask, jsonify, request
from dbutils.execute import execute_select_query, execute_query

app = Flask(__name__)

@app.get('/')
def homepage():
    return "Welcome to IoT Application"

@app.get('/temperatures')
def get_tempeartures():
    query = f"select * from sensorsLog where type = 'LM35';"

    temps = execute_select_query(query)

    return jsonify(temps)

# @app.post('/temperatures/<float:temperature>')
# def insert_temperature(temperature):
#     query = f"insert into sensorsLog(type, location, value) values('LM35', 'Nira', {temperature});"

#     execute_query(query)

#     return "Temperature is added successfully !!!"

@app.post('/temperatures')
def insert_temperature():

    temperature = request.form.get('temperature')

    query = f"insert into sensorsLog(type, location, value) values('LM35', 'Nira', {temperature});"

    execute_query(query)

    return "Temperature is added successfully !!!"


app.run(host='0.0.0.0', port=4000, debug=True)
