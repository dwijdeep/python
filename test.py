#count the number with highest occurrence in list 
l=[1,2,3,1,5,5,1,7,2,9,9,9,9]
l.sort()
s=set(l)
li=[]
#print(set(l))
for i in s:
    li.append(l.count(i))
#print(li)
a=max(li)
x=li.index(a)
lis=list(s)
print(lis[x])