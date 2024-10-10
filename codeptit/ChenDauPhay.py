
n = int(input())
stack = []

while(n != 0):
	stack.append(n%1000)
	n //= 1000

print(stack.pop(), end= "")
while(len(stack) != 0):
	print(",%03d"%stack.pop(), end="")
