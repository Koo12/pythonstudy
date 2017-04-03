def triangles(n):
	if n==1:
		print([1])
	if n==2:
		print([1])
		print([1,1])
	if n>=3:
		print([1])
		print([1,1])
		L=[1,2,1]
		L1=L[:]
		print(L)
		c=0
		while c<n-3:
			a=1
			L=L1[:]
			while a<len(L1):
				b=a-1
				L1[a]=L[b]+L[a]
				a=a+1
			L1.append(1)	
			print(L1)
			c=c+1
N=input('请输入你想要输出几行杨辉三角？')
N=int(N)
triangles(N)