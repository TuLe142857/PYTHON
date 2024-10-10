
digits = [ 
	'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
	'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
	'U', 'V', 'W', 'X', 'Y', 'Z']

def convert(n, base):
	s = ""
	while(n != 0):
		s = digits[n%base] + s
		n //= base
	return s

for nTest in range(int(input())):
	n, base = map(int, input().split())
	print(convert(n, base))