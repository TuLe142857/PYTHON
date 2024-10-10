import string

def encrypt(s):
	s_ = ""
	i = 0

	c = s[0]
	count = 0
	while(i < len(s)):
		while(i < len(s) and s[i] == c):
			i += 1
			count += 1
		s_ += str(count) + c
		if(i ==  len(s)):
			break
		c = s[i]
		count = 0

	return s_

for nTestCase in range(int(input())):
	print(encrypt(input()))