p,a=map(str,input().split())
gh=0
if len(p)>len(a):
  p,a=a,p
c=0
while c<len(p):
  gh+=(ord(a[c])-ord(p[c]))
  c+=1
for c in range(c,len(a)):
  gh+=ord(a[c])-ord('a')+1
print(gh)
