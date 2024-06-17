#!/usr/bin/env python3
# fahrenheit_to_celsius.py

for fahrenheit in range(-44, 217, 4):
    # every integer in the range of -44 to 216 (increment: 4) undergoes
    # the following process laid out by this following scope
    celsius = (fahrenheit - 32) * 5 / 9
    # Do math on the integer to define new variable "celsius"
    print(f"{fahrenheit:>6.2f} F = {celsius:>6.2f} C")
    # Print f string; each F is right indented 6 point font, 2 digits
    # after decimal. Same for each celsius
