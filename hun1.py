p=int(input())
o=[]
for h in range(0,p):
 pan=input()
 o.append(pan)
ven1=[]
for h in zip(*o):
 if(h.count(h[0])==len(h)):
  ven.append(h[0])
 else:
  break
print(''.join(ven1))
