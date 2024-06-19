#!/usr/bin/env python3
# celsius_to_fahrenheit.py

for celsius in range(-44, 110, 4): #celsius range, in increment of 4
    fahrenheit = (celsius * (9/5)) + 32 #convert each celsius to fahrenheit
    print(f"{celsius:>6.2f} C = {fahrenheit:>6.2f} F")
 