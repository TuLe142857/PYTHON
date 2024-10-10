import math
def check(n):
    digits =int(math.log(n,10)) + 1
    return (n%100 == n//math.pow(10, digits - 2))
    
for i in range(int(input())) :
     if(check(int(input()))):
         print("YES") 
     else:
         print("NO")    