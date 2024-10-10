import string

def charToInt(c):
	return int(c) - int('0')
def decrypt(s):
	s_ = ""
	i = 0
	while(i < len(s)):
		for j in range(0, charToInt(s[i+1])):
			s_ += s[i]
		i += 2
	return s_

for nTestCase in range(int(input())):
	print(decrypt(input()))
