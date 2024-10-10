import math

def isPrime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if(n % i == 0):
			return False
	return True

def doiXung(n):
	n_ = 0
	while(n != 0):
		n_ = n_*10 + n%10
		n //= 10
	return n_

for nTestCase in range(int(input())):
	n = int(input())
	arr = []
	for i in range(n):
		i_ = doiXung(i)
		if(i >= i_ or i_ >= n):
			continue
		if(isPrime(i) and isPrime(i_)):
			arr.append(i)
			arr.append(i_)
	for x in arr:
		print(x, end = " ")
	print()