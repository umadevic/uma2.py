d,e=input().split()
jk1=abs(len(e)-len(d))
for g in range(len(d)):
    if(len(e)==1 and e[g] in d):
        break
    if (d[g]!=e[g]):
        jk1=jk1+1
print(jk1)
