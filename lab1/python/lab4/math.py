import math

x = int(input("Input Degree: "))
print("Output radian:", math.radians(x))

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print((a+b)*h/2)

n = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
print("The area of the polygon is: ", round((n * length ** 2) / (4 * math.tan(math.pi/h))))

l = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
print(l * h)
