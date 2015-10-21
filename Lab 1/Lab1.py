from math import *

l = float(input("Enter your latitude: "))
h = float(input("Enter your height: "))

Re = 6378100 * cos(radians(l))
asec_angle = h/Re + 1
asec_result = acos(1/asec_angle)
day = 24*60*60
v = (2*pi*h)/(day*asec_result)
t = h/v

print("your speed to reach your height is", v, "your time to reach your height is", t)