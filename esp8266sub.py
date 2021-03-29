from umqtt.simple import MQTTClient


def msg(a,b):
 print(str(b,'utf-8'))


server="MQTT Broker ip address or Hostname"
c = MQTTClient("umqtt_client", server)
c.set_callback(msg)
c.connect()
c.subscribe("test2")

c.wait_msg()

c.check_msg()
       
c.disconnect()
