import math
n = int(input())
arr = list(map(int, input().split()))

minStep = -1
value = 0

for tryValue in arr:
	count = 0
	for x in arr:
		count += abs(x - tryValue)
		if(count >= minStep and minStep != -1):
			break
	if(count < minStep or minStep == -1):
		minStep = count
		value = tryValue

print(minStep, " ", value)
