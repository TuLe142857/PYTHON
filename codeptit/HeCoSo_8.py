
def convert(n):
	x = 0

	x += (n%10)*1
	n //= 10

	x += (n%10)*2
	n //= 10

	x += (n%10)*4
	n //= 10

	return x

n = int(input())
stack = []

while(n != 0):
	stack.append(n%1000)
	n //= 1000

while(len(stack) != 0):
	print(convert(stack.pop()), end = "")