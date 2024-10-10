
for nTesCase in range (int(input())):
	s = input()
	stack = []
	stt = 1	
	for c in s:
		if(c == "("):
			print(stt, end = " ")
			stack.append(stt)
			stt += 1
		if(c == ")"):
			print(stack.pop(), end = " ")
	print()




