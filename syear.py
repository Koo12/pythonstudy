A=['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
B=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
C=input('请输入年份')
C=int(C)
D=C-1998 #经过的年份
Tiangan=D%12
Dizhi=D%10
if Dizhi>=6:
	Dizhi=Dizhi-10
if Tiangan>=10:
	Tiangan=Tiangan-12
print('今年的天干地支纪年法为：',A[4+Dizhi],B[2+Tiangan],'年')
