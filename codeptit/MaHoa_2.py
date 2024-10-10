import string
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

def indexOf(c):
	if(c >= 'A' and c <= 'Z'):
		return ord(c) - ord('A')
	if(c == '_'):
		return 26
	return 27

def encrypt(s, k):
	s_ = ""
	# for i in range(len(s)-1, -1, -1):
	# 	s_ += P[(i+k)%28]
	# return s_
	for i in range(len(s)-1, -1, -1):
		index = indexOf(s[i])
		s_ += P[(index + k)%28]
	return s_

def getInput():
	s = input()
	if(s == "0"):
		return int(0), ""
	s_ = s.split()
	return int(s_[0]), s_[1]

k, s = getInput()
while(k != 0):
	print(encrypt(s, k))
	k, s = getInput()