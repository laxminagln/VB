import paho.mqtt.client as mqtt
import time
from pkg_ros_iot_bridge.msg import myMessage

broker_url = "broker.mqttdashboard.com"
broker_port = 1883
pub_message = ""
pub_topic = "/eyrc/ApAnGoLa/ros_to_iot"

def pub() :
	def on_publish(client, userdata, mid):
    		print("--- Publisher ---")
    		print("[INFO] Topic: {}".format(pub_topic))
    		print("[INFO] Message Published: {}".format(pub_message))
    		print("------------")
	pub_client = mqtt.Client()
	pub_client.on_publish = on_publish
	pub_client.connect(broker_url, broker_port)

	while True:
    		pub_message = time.asctime( time.localtime(time.time()) )
    		pub_client.publish(topic=pub_topic, payload=pub_message, qos=0, retain=False)
    		time.sleep(1)

	print("Out of Loop. Exiting..")

def sub() :
	def on_connect(client, userdata, flags, rc):
    		print("[INFO] Connected With Result Code: " + str(rc))

	def on_message(client, userdata, myMessage):
    		print("--- Subscriber ---")
    		print("[INFO] Topic: {}".format(myMessage.topic) )
    		print("[INFO] Message Recieved: {}".format(myMessage.payload.decode()))
    		print("------------")

	sub_client = mqtt.Client()
	sub_client.on_connect = on_connect
	sub_client.on_message = on_message
	sub_client.connect(broker_url, broker_port)

	sub_client.subscribe("/eyrc/ApAnGoLa/iot_to_ros", qos=0)

	sub_client.loop_forever()

	print("Out of Loop. Exiting..")

if __name__ == '__main__':
	pub()
	sub()
