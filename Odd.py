a,n=input().split()
a=int(a)
n=int(n)
if(a<=10000 and n<=10000):
	for i in range(a,n):
		if(i%2==0):
			print(i,end=" ")
else:
	print("no")
