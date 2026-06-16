import math
def area(radius):
    area = math.pi * radius ** 2
    return area
    print('The area of the circle is ', area)


radius = float(input('Enter radius of circle: '))
result = area(radius)
print(f"Area of the circle of radius {radius} is  {result:.2f}")
