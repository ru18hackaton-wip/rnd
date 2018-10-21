#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank

def movemeter(tank):
    tank.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 2)

def turn(tank):
    tank.on_for_rotations(SpeedPercent(0), SpeedPercent(100),2)

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

movemeter(tank_drive)
turn(tank_drive)
movemeter(tank_drive)
