import wifi
import socketpool
from secrets import secrets
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import networking
from node_config import *

# networking.connect_to_network()
# networking.mqtt_initialize()
# networking.mqtt_connect()

# TODO: probably want some global variables here...

# pool = socketpool.SocketPool(wifi.radio)
# mqtt_client = MQTT.MQTT(
#     broker=secrets["mqtt_broker"],
#     port=secrets["port"],
#     # username=secrets["aio_username"],
#     # password=secrets["aio_key"],
#     socket_pool=pool,
#     # ssl_context=ssl.create_default_context(),
# )


# Called when an MQTT message is received.
# topic is the feed name the message was published on.
# message is the contents of the message.
def message_received(client, topic, message):
    print(f"New message on topic {topic}: {message}")

    # TODO: Parse the feed name and take action


# TODO: set up networking, subscribe to feeds, and send initial feed messages


# Run the regular primary control node tasks
def loop():
    # TODO: throttle this loop? (i.e. don't run it every time)

    # print("Executing primary control node loop")

    # TODO: Main temperature control logic

    pass
