import paho.mqtt.client as mqtt

MQTT_ADDRESS = '192.168.43.82'
MQTT_USER = 'sunder'
MQTT_PASSWORD = 'sunder'
MQTT_TOPIC = '+/+/+'

def on_connect(client, userdata, flags, rc):
	print('connected')
	client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload, 'utf-8'))

def main():
	mqtt_client = mqtt.Client()
	mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
	mqtt_client.on_connect = on_connect
	mqtt_client.on_message = on_message
	mqtt_client.connect(MQTT_ADDRESS, 1883)
	mqtt_client.loop_forever()

if __name__ == '__main__':
	print('ads')
	main()
