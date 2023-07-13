# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_hs3003 import hs3003

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
hs = hs3003.HS3003(i2c)

while True:
    temperature, relative_humidity = hs.measurements
    print(f"Temperature: {temperature:.1f}C")
    print(f"Humidity: {relative_humidity:.1f}%")
    print("")
    time.sleep(1)
