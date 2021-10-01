l=[1,5,3]
u=l
u.sort()
b=u[2] #5 star
a=u[0] #1
c=u[1] #3
for i in range(b):
	for j in range(3):
		if(a!=b):
			print("- ")
			a+=1
		else:
			print("* ")