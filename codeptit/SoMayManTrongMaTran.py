rows, columns = map(int, input().split())
arr = []
for i in range(rows):
	arr.append(list(map(int, input().split())))

min = arr[0][0]
max = arr[0][0]
for i in range(rows):
	for j in range(columns):
		if(arr[i][j] > max):
			max = arr[i][j]
		if(arr[i][j] < min):
			min = arr[i][j]

luckyValue = max - min
exist = False
vitri = []
for i in range(rows):
	for j in range(columns):
		if(arr[i][j] == luckyValue):
			vitri.append([i, j])
			exist = True

if(exist):
	print(luckyValue)
	for a in vitri:
		print("Vi tri [%d][%d]"%(a[0], a[1]))
else:
	print("NOT FOUND")