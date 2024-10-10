
factorical = [1]
for i in range(1, 10):
	factorical.append(factorical[i-1] * i)

def isKrish(n):
	sum = 0
	temp = n
	while True:
		sum += factorical[temp%10]
		temp = temp//10
		if(temp == 0):
			break
	return (sum == n)

nTest = int(input())
for i in range(0, nTest):
	if(isKrish(int(input()))):
		print("Yes")
	else:
		print("No")
