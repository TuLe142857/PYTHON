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



for i in range(int(input())):
	x1, y1, x2, y2 = map(float, input().split())
	print("%.04f"%((Point(x1, y1) - Point(x2, y2)).length()))
