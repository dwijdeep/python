#Write a Java program to the right that rotates the elements of an array by N.
input="racecar"
a=[]
for i in input:
    a.append(i)
count=0
#[2,3,4,5,6,1]
#[3,4,5,6,1,2]
#[4,5,6,1,2,3]

#print(a[n:]+a[0:n])
b=[]
print(a[0])
print(a[1])
while(a[0]!=a[-1] or count!=len(a)):
    for i in range(len(a)-1):
        b.append(a[i+1])
    b.append(a[0])
    count+=1
    #print(b)
    if(count!=len(a)):
        a=b
        b=[]
    
print("".join(b))