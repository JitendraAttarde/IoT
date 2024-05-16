from flask import Flask,request
from dbutils.execute 


srv = Flask(__name__)


@srv.route('/',methods = ['GET'])
def homepage():
    return "Welcome to Fitness Tracker"

@srv.route('/add',methods = ['POST'])
def add_info():
    name = request.get_json().get('name')
    age = request.get_json().get('age')
    city = request.get_json().get('city')
    steps = request.get_json().get('steps')
    pulse = request.get_json().get('pulse')
    oxygen = request.get_json().get('oxygen')  
    temperature = request.get_json().get('temperature')  

    query = f"insert into health (name, age, steps, pulse, oxygen, temp) values('{name}', {age}, {city}, {steps}, {pulse}, {oxygen}, {temperature});"

    execute_query(query=query)

    mqttc.connect("localhost");
    mqttc.publish("health/status","GET : success")
    mqttc.disconnect()
    return "Health parameter is successfully added"

@srv.route('/all',methods = ['GET'])
def get_all():
    query = f"select * from health;"

    mqttc.connect("localhost")
    mqttc.publish("health/status","GET: success")
    mqttc.disconnect()
    return jsonify(execute_select_query(query=query))

@srv.route('/update',methods = ['PUT'])
def update_city():
    name = request.form.get('name')
    city = request.from.get('city')

    query = f"upadate health SET city = '{city}' where name = '{name}';" 
       

