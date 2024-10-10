def check(text):
	s = text.split(".")
	if(len(s) != 4):
		return False
	for s_ in s:
		if(not s_.isdigit()):
			return False
		value = int(s_)
		if(not(value >= 0 and value <= 255)):
			return False
	return True

for i in range(int(input())):
	if(check(input())):
		print("YES")
	else:
		print("NO")
		