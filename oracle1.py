l=[1,2,3,5]

x=l[0]#1
y=l[-1]#5
for i in range(1,y):
	if i not in l:
		print(i)