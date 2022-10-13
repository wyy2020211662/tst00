
import math
n=int(input())
a=["" for i in range (n)]

a=sorted(list(map(int, input().split( ))))
print(a)
n=math.ceil(n/2)

num=0
j=int()
for j in range (n):
    num+=math.ceil(a[j]/2)
print(num)

