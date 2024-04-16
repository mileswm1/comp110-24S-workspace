"""CQ08 - Intro To Object Oriented Programming."""

from lessons.CQ08.point import Point


point = Point(5.0, 8.0)

print("x:", point.x)
print("y:", point.y)

factor = 3
point.scale_by(factor)
print("x:", point.x)
print("y:", point.y)

factor = 4
scaled_point = point.scale(factor)
print("x:", scaled_point.x)
print("y:", scaled_point.y)