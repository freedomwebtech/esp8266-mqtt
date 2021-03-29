from umqtt.simple import MQTTClient
import hcsr04
from time import sleep
server = "192.168.0.100"

topic = "test2"

ultrasonic = hcsr04.HCSR04(trigger_pin =5,echo_pin=4,echo_timeout_us=1000000)
distance = ultrasonic.distance_cm()
u = (str(distance)[0:3]+ "cm")
msg = (bytes(u,'utf-8'))
print(u)
c = MQTTClient("esp8266",server)
c.set_callback(topic)
c.connect()
c.publish(topic,msg)
