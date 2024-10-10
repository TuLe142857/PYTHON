
def sumDigit(n):
	sum = 0
	while(n != 0):
		sum += n%10
		n //= 10
	return sum

for nTestCase in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort(key = lambda a : (sumDigit(a), a))
	for i in arr:
		print(i, end = " ")
	print()