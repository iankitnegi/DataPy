# Given the side length x find the area of hexagon using funn

import math

def area_of_hexagon(s):
    area = 1.5 * math.sqrt(3) * s**2
    return round(area,1)

print(area_of_hexagon(1))
print(area_of_hexagon(2))
print(area_of_hexagon(3))