#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor
import time

color = ColorSensor()
while True:
    try:
        print(color.reflected_light_intensity)
    except ZeroDivisionError as detail:
        print('Handling run-time error:', detail)
    print("\n")
    time.sleep(1)
