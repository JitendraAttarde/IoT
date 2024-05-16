# import mqqt client
import paho.mqtt.client as mqtt

# create instance of mqtt client
mqttc = mqtt.Client("Publisher")

def on_publish(client, userdata, mid):
    print("Message is published successfully")

mqttc.on_publish = on_publish

# connect client with broker
mqttc.connect(host="localhost")

# publish message on topic
mqttc.publish("sensor/temperature", "40")

# disconnect the client
mqttc.disconnect()