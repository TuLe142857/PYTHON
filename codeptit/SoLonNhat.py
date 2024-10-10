import string
def isInt(c):
	return (c >= '0' and c <= '9')

def convert(c):
	return int(c) - int('0')

def findMin(s):
	i = 0
	min = -1
	while(i < len(s)):
		if(not isInt(s[i])):
			i += 1
			continue
		test = 0
		while(i < len(s) and isInt(s[i])):
			test = test * 10 + convert(s[i])
			i += 1
		if(test > min or min == -1):
			min = test
		i += 1
	return min

nTest = int(input())
for i in range(nTest):
	print(findMin(input()))