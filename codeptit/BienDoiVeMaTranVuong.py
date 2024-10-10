
rows, columns = map(int, input().split())
a = [[0 for _ in range(columns)] for _ in range(rows)]

for i in range(rows):
	a[i] = list(map(int, input().split()))

r = [True]*rows
c = [True]*columns
r_ = rows
c_ = columns
# r le, c chan

if(rows < columns):
	for i in range(len(c)):
		if(i % 2 == 1):
			columns -= 1
			c[i] = False
			if(columns == rows):
				break

elif(columns < rows):
	for i in range(len(r)):
		if(i % 2 != 1):
			rows -= 1
			r[i] = False
			if(columns == rows):
					break

# print("------------------------------")
for i in range(r_):
	if(not r[i]):
		continue
	for j in range(c_):
		if(r[i] and c[j]):
			print(a[i][j], end = " ")
	print()