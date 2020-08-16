n,m = (int(i) for i in input().split())
lst = map(int,input().split(" "))
a = set(map(int,input().split(' ')))
b = set(map(int,input().split(' ')))
res = 0
for i in lst:
    if (i in a):
        res+=1
    if (i in b):
        res-=1
print(res)
