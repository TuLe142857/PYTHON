import math

def check(n):
	# duyet tu phai sang trai
	#status = 1 tang
	#status = -1
	status = 1

	if((int(math.log(n, 10)) + 1) < 3):
		return False
	last = n % 10
	n //= 10

	# tang dan
	while(n != 0 and status == 1):
		if(not(last - (n%10) < 0)):
			status = -1
			break
		last = n%10
		n //= 10
	
	# giam dan
	while(n != 0 and status == -1):
		if(not (last - (n%10) > 0 )):
			return False
		last = n%10
		n //= 10
	return True

for nTest in range(int(input())):
	n = int(input())
	if(check(n)):
		print("YES")
	else:
		print("NO")