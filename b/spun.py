#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_D, MediumMotor

spinner = MediumMotor(OUTPUT_D)
spinner.on(-10)

while True:
    pass
