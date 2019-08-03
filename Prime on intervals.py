n,r=input().split()
n,r=int(n),int(r)
for i in range(n,r+1):
	if(i>1):
		for j in range(2,i):
			if(i%j==0):
				break
			else:
				print(i)
				break
