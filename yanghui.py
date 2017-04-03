def triangles(n):
	if n==1:
		yield [1]
	if n==2:
		yield [1]
		yield [1,1]
	if n>=3:
		yield [1]
		yield [1,1]
		L=[1,2,1]
		L1=L[:]
		yield L
		c=0
		while c<n-3:
			a=1
			L=L1[:]
			while a<len(L1):
				b=a-1
				L1[a]=L[b]+L[a]
				a=a+1
			L1.append(1)	
			yield L1
			c=c+1
N=input('请输入你想要输出几行杨辉三角？')
N=int(N)
for t in triangles(N):
	print(t)