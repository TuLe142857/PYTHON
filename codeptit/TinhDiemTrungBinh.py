n = int(input())
arr = list(map(float, input().split()))

sum = 0.0
min = arr[0]
max = arr[0]
nmin = 0	#so lan xuat hien cua min
nmax = 0	#so lan xuat hien cua max

for i in arr:
	sum += i
	if(i == min):
		nmin += 1
	elif(i < min):
		min = i
		nmin = 1
	
	if(i == max):
		nmax += 1
	elif(i > max):
		max = i
		nmax = 1

avg = (sum - min*nmin - max*nmax)/(n - nmin - nmax)
print("%.02f"%avg)