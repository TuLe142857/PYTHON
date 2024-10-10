import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

	def __str__(self):
		return f"({self.x}, {self.y})"
	
	def __repr__(self):
		return f"({self.x}, {self.y})"
	
	def length(self):
		return math.sqrt((self.x)**2 + (self.y)**2)
	
	# check 2 vector cung phuong
	@staticmethod
	def hasSameDirection(a, b):
			# return ((a.x)/(b.x) == (a.y)/(b.y))
			return (a.x*b.y == a.y*b.x)

class Triangle:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	


	@staticmethod
	def isTriangle(t):
		AB = (t.a - t.b).length()
		BC = (t.b - t.c).length()
		AC = (t.a - t.c).length()
		vectorAB = t.b - t.a
		vectorAC = t.c - t.a
		return ((AB + BC > AC) and (not Point.hasSameDirection(vectorAB, vectorAC)))
		
	@staticmethod
	def perimeter(t):
		AB = (t.a - t.b).length()
		BC = (t.b - t.c).length()
		AC = (t.a - t.c).length()
		return (AB + BC + AC)

a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for index in range(t):
	t = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
	if(Triangle.isTriangle(t)):
		print("%.03f"%round(Triangle.perimeter(t), 3))
	else:
		print("INVALID", t.a, t.b, t.c)
	i += 6
