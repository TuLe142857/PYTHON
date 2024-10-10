from math import log as log

def calc(n):
	tong = 0
	tich = 0

	digits = int(log(n, 10)) + 1
	if(digits % 2 != 0):
		tong = n%10
		n //= 10

	while(n != 0):
		if(n%10 != 0):
			if(tich == 0):
				tich = (n%10)
			else:
				tich *= (n%10)
		n //= 10

		tong += n%10
		n //= 10
	print(tong, tich)

for nTest in range(int(input())):
	calc(int(input()))

