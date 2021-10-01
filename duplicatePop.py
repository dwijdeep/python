#remove duplicate elements

l=[1,5,6,9,6,8]

for i in range(len(l)):
	for j in range(i+1,len(l)-1):
		if l[i]==l[j]:
			l.pop(i)
#to verify answer
#print(set(l))
print(l)