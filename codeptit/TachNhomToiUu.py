import math
nTest, k = map(int, input().split())

# arr = []
# for i in range (nTest):
# 	arr.append(int(input()))
arr = list(map(int, input().split()))

arr.sort()

count = 1
last = arr[0]
i = 1

while(True):
	while(i < len(arr) and (arr[i]-arr[i-1]) <= k):
		#print(arr[i], end = " ")
		i += 1
	#print("\n----")
	if(i == len(arr)):
		break
	#print(arr[i], end = " ")
	i += 1
	count += 1

print(count)
