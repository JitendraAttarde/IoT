from flask import Flask,request,jsonify
from dbutils.execute import execute_query,execute_select_query
import paho.mqtt.client as mqtt


srv = Flask(__name__)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Test")


@srv.route('/',methods = ['GET'])
def homepage():
    mqttc.connect("localhost");
    mqttc.publish("wheather/rain","GET : success")
    mqttc.disconnect()
    return "Welcome to To Wheather Rain"

@srv.route('/store',methods = ['POST'])
def add_info():
    humid = request.get_json().get('humid')
    mintemp = request.get_json().get('mintemp')
    maxtemp = request.get_json().get('maxtemp')
    rainfall = request.get_json().get('rainfall')
    evaporation = request.get_json().get('evaporation')
    sunshine = request.get_json().get('sunshine')
    humidity = request.get_json().get('humidity')
    rainToday = request.get_json().get('rainToday')

    query = f"insert into human (humid, mintemp, maxtemp, rainfall, evaporation, sunshine, humidity, rainToday) values({humid}, {mintemp}, {maxtemp}, {rainfall}, {evaporation}, {sunshine}, {humidity}, '{rainToday}');"

    execute_query(query=query)

    mqttc.connect("localhost");
    mqttc.publish("wheather/rain","GET : success")
    mqttc.disconnect()
    return "Wheather Rain parameter is successfully added"   

@srv.route('/display',methods = ['GET'])
def get_all():
    query = f"select * from human;"

    mqttc.connect("localhost");
    mqttc.publish("Wheather/rain","GET : success")
    mqttc.disconnect()
    return jsonify(execute_select_query(query=query))   

@srv.route('/findmin',methods = ['GET'])
def get_info():
    name = request.get_json().get('mintemp')

    query = f"select * from human where mintemp = {mintemp};"
    
    mqttc.connect("localhost");
    mqttc.publish("Wheather/rain","GET : success")
    mqttc.disconnect()
    return jsonify(execute_select_query(query))
  

@srv.route('/humid',methods = ['GET'])
def get_steps():
    #query = f"select * from health order by steps DESC limit 1;"
    query = f"select * from human where maxtemp = {maxtemp}"
    mqttc.connect("localhost")
    mqttc.publish("Wheather/rain", "GET : success")
    mqttc.disconnect()
    return jsonify(execute_select_query(query))

if __name__ == '__main__':
    srv.run(host='0.0.0.0',port=3000,debug=True)    