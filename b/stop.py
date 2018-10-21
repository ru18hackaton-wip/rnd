#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank

tank = MoveTank(OUTPUT_A, OUTPUT_B)
tank.off()
