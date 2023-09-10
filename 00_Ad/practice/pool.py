import math

x1, y1, x2, y2 = 0, 0, 3, 2

r = math.sqrt((x2-x1)**2 + (y2-y1)**2)
tan_c = math.atan((y2-y1)/(x2-x1))
rad_c = math.radians(tan_c)
deg_c = math.degrees(rad_c)
print(tan_c)
print(rad_c)
print(deg_c)