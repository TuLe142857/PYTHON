import string

s = input()
k = int(input())
arr = [0] * 100

size = len(s) - len(s)%2
i = 1
while(i < len(s)):
	arr[int(s[(i-1): (i+1)])] += 1
	i += 2

exist = False
for i in range(10, 100):
	if(arr[i] >= k):
		print(i, " ", arr[i])
		exist = True
if(not exist):
	print("NOT FOUND")
