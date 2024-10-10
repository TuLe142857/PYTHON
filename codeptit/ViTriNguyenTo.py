import math

def isPrime(n):
	if(n < 2):
		return False
	for i in range(2, int(math.sqrt(n))+1):
		if(n %i == 0):
			return False
	return True


for n in range(int(input())):
	s = input()
	check = True
	for i in range(0, len(s)):
		value = int(s[i]) - int('0')
		check_value = isPrime(value)
		check_index = isPrime(i)
		if(not((check_value and check_index) or (not check_value and not check_index))):
			check = False
			
		if(not check):
			break

	if(check):
		print("YES")
	else:
		print("NO")
