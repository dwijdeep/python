s="aabbbcdd"
#a2b3c1d2	
dict ={}
out=""
for i in s:
    if i in dict.keys():
        dict[i]+=1
    else:
        dict[i]=1
for i in dict:
    out+=i+str(dict[i])

print(str(out))
