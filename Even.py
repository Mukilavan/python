a,n=input().split()
a=int(a)
n=int(n)
for i in range(a,n):
	if(i%2==0 and i!=a):
		print(i,end=" ")

