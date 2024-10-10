def gcd(a, b):
	while(b != 0):
		temp = a % b
		a = b
		b = temp
	return a

def reverse(n):
	n_ = 0
	while(n != 0):
		n_ = 10*n_ + n%10
		n //= 10
	return n_

for nTest in range(int(input())):
	n = int(input())
	if(gcd(n, reverse(n)) == 1):
		print("YES")
	else:
		print("NO")
