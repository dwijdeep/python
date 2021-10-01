str="My name is Rajat"
l=[]
for item in str:
    l.append(item)

for i in range(len(l)):
	for j in range(i+1,len(l)):
		if l[i]>l[j]:
			l[i],l[j]=l[j],l[i]

print(l)