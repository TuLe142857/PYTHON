
nA, nB = map(int, input().split())
A = [False]*1000
B = [False]*1000

strA = list(map(int, input().split()))
strB = list(map(int, input().split()))

for x in strA:
	A[x] = True
for x in strB:
	B[x] = True

#A giao B
for i in range(0, 1000):
	if(A[i] and B[i]):
		print(i, "", end="")
print()

# A\B
for i in range(0, 1000):
	if(A[i] and (not B[i])):
		print(i, "", end = "")
print()

# B\A
for i in range(0, 1000):
	if(B[i] and (not A[i])):
		print(i, "", end = "")
