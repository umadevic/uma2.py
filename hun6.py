num9=int(input())
array=list(map(int,input().split()))
b2=0
for n3 in range(len(array)-2):
    for i in range(n3+1,len(array)-1):
        for l in range(i+1,len(array)):
            if array[n3]<array[i]<array[l] and n3<i<l:
                b2=b2+1
print(b2)
