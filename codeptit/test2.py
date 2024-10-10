from collections import deque
import heapq

class Matrix:
    def __init__(self, rows, columns, value):
        self.rows = rows
        self.columns = columns
        self.value = value

    def validIndex(self, index):
        return(index.i >= 0 and index.i < self.rows and index.j >= 0 and index.j < self.columns)

    def getValue(self, index):
        return self.value[index.i][index.j]

class Index:
    def __init__(self, i, j):
        self.i = i
        self.j = j
     
    def __add__(self, o):
        return Index(self.i + o.i, self.j + o.j)

    def __mul__(self, k):
        return Index(k*self.i, k*self.j)

    def __str__(self):
        return f"({self.i}, {self.j})"

class Try:
    def __init__(self, idx, step, l):
        self.idx = idx
		self.step = step
		self.l = l
	def __lt__(self, o):
		return (self.l < o.l)

GO = [Index(0, 1), Index(1, 0), Index(1, 1)]
def calculate(matrix):
    if(matrix.rows == 1 and matrix.columns == 1):
        return 0
    
    # queue = [Try(Index(0, 0), 0)]
    # queue = deque()
    # queue.append(Try(Index(0, 0), 0))
    while(len(queue) != 0):
        x = queue.popleft()
        idx = x.idx
        step = x.step+1

        for go in GO:
            if(not matrix.validIndex(idx + go)):continue
            d = abs(matrix.getValue(idx) - matrix.getValue(idx + go))
            if(d == 0): continue
            next = idx + go*d
            if(not matrix.validIndex(next)): continue

            if(next.i == matrix.rows-1 and next.j == matrix.columns-1):
                return step
            queue.append(Try(next, step))
    return -1

# matrix = Matrix(3, 3, [[2, 1, 2], [1, 2, 4], [1, 3, 2]])
# print(calculate(matrix))

# matrix = Matrix(1, 1 ,[[1]])
# print(calculate(matrix))

for nTest in range(int(input())):
    rows, columns = map(int, input().split())
    value = [ [int(i) for i in input().split()] for x in range(rows)]
    print(calculate(Matrix(rows, columns, value)))