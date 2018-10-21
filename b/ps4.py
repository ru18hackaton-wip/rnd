#!/usr/bin/env python3

# Original author of random wiki post we did use as base layout
__author__ = "bythew3i"

import evdev

from ev3dev2.motor import MoveJoystick, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D


# Finds the gamepad from Bluetooth device list

def find_controller():
    # ps4 controller set up
    print("Finding ps4 controller...")
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    ps4dev = devices[0].fn

    gamepad = evdev.InputDevice(ps4dev)
    return gamepad


# Initializes our joystick move for vectorial movement of gamepad analog stick

def create_steering_tank():
    jmove = MoveJoystick(OUTPUT_A, OUTPUT_B)
    return jmove


# Scales the analog stick for the controlling module range

def scale(val, src, dst):
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scale_stick(value):
    return scale(value, (0,255),(1, -1))



x = 0
y = 0
print("onks padia")
gamepad = find_controller()
bot = create_steering_tank()
koura = MediumMotor(OUTPUT_D) # our hand to grab 'em all

for event in gamepad.read_loop():   #this loops infinitely

    # Read the analog stick values and move the robot
    if event.type == 3:
        if event.code == 1:
            y = scale_stick(event.value)
        if event.code == 0:
            x = scale_stick(event.value)/3.0

        try:
            bot.on(x, y, 100, 1)
        except TypeError: # thanks to library bug a quick fix
            bot.off()

    # Listen to the trigger to start moving the hand
    if event.type == 1 and event.value == 1:
        if event.code == 312:
            koura.on(-5)
        if event.code == 313:
            koura.on(5)

    # Don't over do, so stop the engine on trigger release
    if event.type == 1 and event.value == 0:
        if event.code == 312:
            koura.stop()
        if event.code == 313:
            koura.stop()
