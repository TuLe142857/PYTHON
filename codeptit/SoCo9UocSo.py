import math

# So chia het cho 9 co hai dang
# n = a^8
# n = a^2 * b^2
# Voi a, b la cac so nguyen to
# => so nguyen to lon nhat co the: 
# 		xet TH n = a^2 * b^2 , 
#			a max = sqrt(max n)/(min b^2); min b = 2
maxValue = 10**9
maxPrime = math.ceil(math.sqrt(maxValue/4))

def isPrime(n):
	if(n < 2):
		return False
	i = 2
	while(i*i <= n):
		if(n%i == 0):
			return False
		i += 1
	return True

def getPrimeArray(n):
	prime = []
	for i in range(2, n+1):
		if(isPrime(i)):
			prime.append(i)
	return prime

prime = getPrimeArray(maxPrime)

# Bat dau tinh
n = int(input())
count = 0

def type1(a, b):
	return a*a*b*b
	
for i in range(0, len(prime)):
	for j in range(i+1, len(prime)):
		if(type1(prime[i], prime[j]) <= n):
			count += 1
		else:
			break # break for(j)


def type2(a):
	return int(math.pow(a, 8))

for i in prime:
	if(type2(i) <= n):
		count += 1
	else:
		break

print(count)

