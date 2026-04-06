import networking
import time
import temperature_measurement_node

functions = [
    temperature_measurement_node.loop,
    networking.loop,
]

while True:
    for f in functions:
        f()
