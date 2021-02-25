#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:24:02 2019

@author: mariapacifico
"""

rod_str = input("Input rods: ")
rod_float = float(rod_str)
print("You input", round(rod_float, 3),
      "rods.")

meters_float = rod_float * 5.0292
furlong_float = rod_float / 40.0
mile_float = meters_float / 1609.34
feet_float = meters_float / 0.3048
walking_float = mile_float / 3.1 * 60.0

print("Conversions")
print( "Meters:", round(meters_float, 3)) 
print("Feet:", round(feet_float, 3) )
print("Miles:", round(mile_float, 3) )
print("Furlongs:", furlong_float)
print("Minutes to walk", round(rod_float, 3),
      "rods:", round(walking_float, 3))