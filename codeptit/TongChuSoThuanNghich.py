def isPalindrome(n):
	if(n < 10):
		return False
	return (n == reverse(n))

def reverse(n):
	r = 0
	while(n != 0):
		r = r*10 + (n%10)
		n //= 10
	return r

def sumDigits(n):
	sum = 0
	while(n != 0):
		sum += n%10
		n //= 10
	return sum

for nTestCase in range(int(input())):
	n = int(input())
	if(isPalindrome(sumDigits(n))):
		print("YES")
	else:
		print("NO")