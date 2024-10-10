
class Matrix:
	def __init__(self, rows, columns):
		self.columns = columns
		self.rows = rows
		self.value = [[0 for _ in range(columns)] for _ in range(rows)]
	
	def tranpose(self):
		arr =  [[self.value[j][i] for j in range(self.rows)] for i in range(self.columns)]
		m = Matrix(self.columns, self.rows)
		m.value = arr
		return m

	def __str__(self):
		s = ""
		for i in range(self.rows):
			for j in range(self.columns):
				s += str(self.value[i][j]) + " "
			if(i != self.rows-1):
				s += "\n"
		return s

	def __mul__(self, o):
		r = self.rows
		c = o.columns
		x = self.columns
		m = Matrix(r, c)
		for i in range(r):
			for j in range(c):
				sum  = 0
				for a in range(x):
					sum += self.value[i][a]*o.value[a][j]
				m.value[i][j] = sum	
		return m

# m = Matrix(2, 2)
# m.value = [[1, 2], [3, 4]]
# print(m)
# print(m.tranpose())
# print((m)*(m.tranpose()))

for nTest in range(int(input())):
	r, c = map(int, input().split())
	arr = [[int(x) for x in input().split()] for _ in range(r)]
	m = Matrix(r, c)
	m.value = arr
	print((m)*(m.tranpose()))