import math

def my_round(n):
	if(n >= 0.5):
		return 1
	return 0

def lamTron(n):
	if( n <= 10 ):
		return n
	digits = int(math.log(n, 10)) + 1
	while(n > 10):
		n /= 10
		n = int(n) + my_round(n - int(n))
	return int(n * math.pow(10, digits-1))
	

for i in range(int(input())):
	print(lamTron(int(input())))
