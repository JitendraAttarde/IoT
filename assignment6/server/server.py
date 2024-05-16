from flask import Flask, request, jsonify
from dbutils.connection import get_connection
from dbutils.execute import execute_query, execute_select_query

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def homepage():
    return "Welcome to IoT Application"

@app.route('/temperature', methods = ['POST'])
def insert_temperature():
    temp = request.get_json().get('temperature')
    location = request.get_json().get('location')

    query = f"insert into sensorsLog(type, location, value) values('LM35', '{location}', {temp});"

    execute_query(query)

    return "Temperature is added successfully"

@app.route('/ldr', methods = ['POST'])
def insert_ldr():
    ldr = request.get_json().get('ldr')
    location = request.get_json().get('location')

    query = f"insert into sensorsLog(type, location, value) values('LDR', '{location}', {ldr});"

    execute_query(query)

    return "LDR value is added successfully"


@app.route('/tempvalues', methods = ['GET'])
def get_temperatures():
    query = f"select  * from sensorsLog where type = 'LM35';"

    return jsonify(execute_select_query(query))

@app.route('/ldrvalues', methods = ['GET'])
def get_ldrvalues():
    query = f"select  * from sensorsLog where type = 'LDR';"

    return jsonify(execute_select_query(query))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)