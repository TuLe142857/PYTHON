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

	@staticmethod
	def area(t):
		AB = (t.a - t.b).length()
		BC = (t.b - t.c).length()
		AC = (t.a - t.c).length()
		p = (AB + BC + AC)/2
		return math.sqrt(p * (p-AB) * (p - BC) * (p - AC))

# for nTest in range(int(input())):
# 	x1, y1, x2, y2, x3, y3 = map(float, input().split())
# 	t = Triangle(Point(x1, y1), Point(x2, y2), Point(x3, y3))
# 	if(Triangle.isTriangle(t)):
# 		print("%.02f"%round(Triangle.area(t), 2))
# 	else:
# 		print("INVALID")

a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for index in range(t):
	t = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
	if(Triangle.isTriangle(t)):
		print("%.2f"%round(Triangle.area(t), 3))
	else:
		print("INVALID")
	i += 6