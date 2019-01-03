import math

class Point(object):
    """Represents a cordination
    of a point.
    """
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __repr__(self):
        return "cordination:({}, {})".format(self.x, self.y)
class Rectangle(Point):
    """Represents a rectangle.
    attributes: width, height, corner.
    """
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

def distance_between_points(P1, P2):
    dx = P1.x - P2.x
    dy = P1.y - P2.y

    dist = math.sqrt(dx**2 + dy**2)
    return dist

def find_center(rect):
    """Find the center of a Rectangle"""
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def grow_rectangle(rect, dwidth, dheight):
    """Changes the dimention of the Rectangle"""
    rect.width += dwidth
    rect.height += dheight

"""write a function named move_rectangle that takes a Rectangle and
two numbers named dx and dy. It should change the location of the rectangle by
adding dx to the x coordinate of corner and adding dy to the y coordinate of corner"""

def move_rectangle(rect, dx, dy):
    """Move the Rectangle by modifying its corner object.

    rect: Rectangle object.
    dx: change in x coordinate (can be negative).
    dy: change in y coordinate (can be negative).
    """
    rect.corner.x += dx
    rect.corner.y += dy


def move_rectangle_copy(rect, dx, dy):
    """Move the Rectangle and return a new Rectangle object.

    rect: Rectangle object.
    dx: change in x coordinate (can be negative).
    dy: change in y coordinate (can be negative).

    returns: new Rectangle
    """
    new = copy.deepcopy(rect)
    move_rectangle(new, dx, dy)
    return new

class Circle(object):
    pass

circle = Circle()
circle.center = Point()
circle.center.x = 150
circle.center.y = 100
circle.raduis = 75

def point_in_circle(circ, point):
    pass

""" Write a function named point_in_circle that takes a Circle and a Point and returns
True if the Point lies in or on the boundary of the circle.

Write a function named rect_in_circle that takes a Circle and a Rectangle and
returns True if the Rectangle lies entirely in or on the boundary of the circle.

Write a function named rect_circle_overlap that takes a Circle and a Rectangle
and returns True if any of the corners of the Rectangle fall inside the circle. Or as a
more challenging version, return True if any part of the Rectangle falls inside the
circle. """


import turtle
bob = turtle.Turtle()
"""
for i in range(4):
    bob.fd(100)
    bob.lt(90)
turtle.mainloop()
"""
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

import math
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)
