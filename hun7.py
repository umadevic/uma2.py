op=int(input())
p=[]
dif1=0
for g in range (0,op+1):
    dif1=abs((2**g)-op)
    p.append(dif1)
kl=min(p)
print(kl)
