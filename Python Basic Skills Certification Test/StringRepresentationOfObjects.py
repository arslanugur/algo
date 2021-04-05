#!/bin/python

import math
import os
import random
import re
import sys



class Car:
    def __init__(self,speed, unit):
        self.speed = speed
        self.unit = unit

    def __str__(self):
        str1 = "Car with the maximum speed of {} {}"
        return str1.format(self.speed,self.unit)

class Boat:
    def __init__(self,speed):
        self.speed = speed
    def __str__(self):
        str1 = "Boat with the maximum speed of {} knots"
        return str1.format(self.speed)

if __name__ == '__main__':#!/bin/python
