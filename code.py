import primary_control_node
import networking
import time
import temperature_measurement_node

functions = [
    temperature_measurement_node.loop,
    networking.loop,
    primary_control_node.loop,
]

while True:
    for f in functions:
        f()
