'''

import math


class Rectangle(object):

    def __init__(self, width, height):

        self.width = width

        self.height = height
        

class Circle(object):

    def __init__(self,diameter):

        self.diameter = diameter

    def area(self):

        r = self.diameter/2

        return math.pi*r*r

'''



class Trip(object):

    def __init__(self, code, day_out, mount_out, year_out, days, cost):

        self.code = code

        self.day_out = day_out

        self.days = days

        self.cost = cost
        