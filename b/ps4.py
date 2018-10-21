#!/usr/bin/env python3
__author__ = "bythew3i"

import evdev

from ev3dev2.motor import MoveJoystick, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D

def find_controller():
    # ps4 controller set up
    print("Finding ps4 controller...")
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    ps4dev = devices[0].fn

    gamepad = evdev.InputDevice(ps4dev)
    return gamepad

def create_steering_tank():
    jmove = MoveJoystick(OUTPUT_A, OUTPUT_B)
    # jmove.set_polarity(LargeMotor.POLARITY_INVERSED)
    return jmove


def scale(val, src, dst):
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scale_stick(value):
    return scale(value, (0,255),(1, -1))



x = 0
y = 0
print("onks padia")
gamepad = find_controller()
bot = create_steering_tank()
koura = MediumMotor(OUTPUT_D)
speed = 30

for event in gamepad.read_loop():   #this loops infinitely
    if event.type == 3:             #Some stick is moved
        if event.code == 1:         #Y axis on right stick
            perkele = scale_stick(event.value)
            wheel_speed = perkele
            y = perkele
        if event.code == 0:
            perkele2 = scale_stick(event.value)/3.0
            steer_speed = perkele2
            x = perkele2
        try:
            bot.on(x, y, 100, 1)
        except TypeError:
            bot.off()

    if event.type == 1 and event.value == 1:
        if event.code == 312:
            print("kiinni")
            koura.on(-5)
            print("kiinnien")
        if event.code == 313:
            print("auki")
            koura.on(5)
            print("aukien")
    
    if event.type == 1 and event.value == 0:
        if event.code == 312:
            print("kiinni")
            koura.stop()
            print("kiinnien")
        if event.code == 313:
            print("auki")
            koura.stop()
            print("aukien")
