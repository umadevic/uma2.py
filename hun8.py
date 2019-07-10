import math
n99,m99=map(int,input().split())
op=[]
gg=list(map(int,input().split()))
for i in range(0,m99):
    l,h=map(int,input().split())
    op.append([l,h])
for i in op:
    kk=i[0]-1
    ll=i[1]-1
    print(math.gcd(gg[kk],gg[ll]))
