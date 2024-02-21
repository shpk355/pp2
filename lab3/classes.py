class Sol1:
    s: str

    def get_string(self):
        a = input()
        self.s = a

    def print_string(self):
        print(self.s)
# p = Sol1()
# p.get_string()
# p.print_string()

class Shape:
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length**2)

# p = Square(4)
# p.area()

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

# p = Rectangle(2, 4)
# p.area()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, a, b):
        self.x = a
        self.y = b
def dist(first, second):
    return ((first.x - second.x)**2 + (first.y - second.y)**2)**0.5
# p = Point(0, 0)
# print(p.x, p.y)
# p.move(2, 2)
# print(p.x, p.y)
# a = Point(6, 8)
# b = Point(3, 4)
# print(dist(a, b))

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, a):
        self.balance+=a

    def withdraw(self, a):
        self.balance-=a
p = Account("sanzhar", 0)
n = int(input())
for i in range(n):
    if i %2 == 0:
        e = int(input())
        p.deposit(e)
    else:
        e = int(input())
        if e>p.balance:
            print("withdrawal of {} is not available".format(e))
        else:
            p.withdraw(e)
arr=[11, 65, 59, 37, 102, 339, 221, 50, 70]
def prime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True
new_arr = list(filter(lambda x: prime(x), arr))
print(new_arr)