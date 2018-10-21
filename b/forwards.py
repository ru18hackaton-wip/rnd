#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, LargeMotor

tank = MoveTank(OUTPUT_A, OUTPUT_B)
tank.set_polarity(LargeMotor.POLARITY_INVERSED)
tank.on(100, 100)

while True:
    pass
