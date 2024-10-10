import math

n = int(input())
digits = int(math.log(n, 10)) + 1
if(digits % 2 != 0):
	n //= 10

arr = [False]*100

while(n != 0):
	arr[n%100] = True
	n //= 100

for i in range(10, 100):
	if(arr[i]):
		print(i, "", end = "")