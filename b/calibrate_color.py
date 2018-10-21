#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor
import time

color = ColorSensor()
color.calibrate_white()
