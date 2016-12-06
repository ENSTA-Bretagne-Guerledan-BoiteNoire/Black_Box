#!/usr/bin/env python


from maestro.maestro import Controller
import time

run = 1

m = Controller('COM1')
while run:
    m.setTarget(0, 2000) # on
    time.wait(2)
    m.setTarget(0, 1000)  # on
    time.wait(2)