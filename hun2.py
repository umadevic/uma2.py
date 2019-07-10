from itertools import combinations
number ,de = input().split()
de = int(de)
nila1 = []
hj = combinations(number,len(number)-de)
for d in hj:
    nila1.append("".join(d))
print(min(nila1))
