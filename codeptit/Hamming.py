import math

maxValue = 10**18
max2 = int(math.log(maxValue, 2))
max3 = int(math.log(maxValue, 3))
max5 = int(math.log(maxValue, 5))
# print(max2, max3, max5)
def count(n):
	c = 0
	for i in range(max2+1):
		for j in range(max3+1):
			for k in range(max5+1):
				if((2**i) * (3**j) * (5**k) <= maxValue):
					c += 1
				else:
					break
	return c

# print(count(maxValue))
# n = count(maxValue)
n = 10917
hamming = [None]*n

count = 0
for i in range(max2+1):
	for j in range(max3+1):
		for k in range(max5+1):
			if((2**i) * (3**j) * (5**k) <= maxValue):
				hamming[count] = (2**i) * (3**j) * (5**k)
				count += 1
			else:
				break
hamming.sort()

# print("count:", count)
def binarySearch(k, arr, n):
	low = 0
	high = n-1
	while(low <= high):
		mid = low + int((high - low)/2)
		if(k == arr[mid]):
			return mid
		if(k < arr[mid]):
			high = mid -1
		else:
			low = mid + 1
	return -1
	
for nTest in range(int(input())):
	# value = int(input())
	# pos = -1
	# for i in range(n):
	# 	if(value == hamming[i]):
	# 		pos = i
	# 		break
	# 	elif(value < hamming[i]):
	# 		break
	pos = binarySearch(int(input()), hamming, n)
	if(pos != -1):
		print(pos+1)
	else:
		print("Not in sequence")



