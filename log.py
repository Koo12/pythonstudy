import math
def quadratic(a,b,c):
	n1=(-b+math.sqrt(b*b-4*a*c))/2*a
	n2=(-b-math.sqrt(b*b-4*a*c))/2*a
	return n1,n2
A=input('输入第一个参数')
B=input('输入第二个参数')
C=input('输入第三个三数')
A=int(A)
B=int(B)
C=int(C)
if B*B-4*A*C>=0:
	x1,x2=quadratic(A,B,C)
	print(x1,x2)
else:
	print('该方程无解')