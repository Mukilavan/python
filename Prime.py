a=int(input())
c=0
for i in range(2,a//2+1):
    if(a%i==0):
        c=c+1
if(c<=0):
    print("yes")
else:
    print("no")
