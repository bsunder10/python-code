import paho.mqtt.client as mqtt

MQTT_ADDRESS = '192.168.43.82'
MQTT_USER = 'sunder'
MQTT_PASSWORD = 'sunder'
MQTT_TOPIC = '+/+/+'

def on_connect(client, userdata, flags, rc):
	print('connected')
	client.subscribe(MQTT_TOPIC)


def main():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.connect(MQTT_ADDRESS, 1883)
    v = input(" sdf ")
    mqtt_client.publish('sunder', v)
    print('done')

while True:
    print('ads')
    main()
