arr = [1, 2, 2, 3, 2, 2, 2, 4, 4,4,4,1]  
#Array fr will store frequencies of element  
freq = [None] * len(arr);  
   
for i in range(len(arr)):  
    count = 1 
    for j in range(i+1, len(arr)):  
        if(arr[i] == arr[j]):  
            count = count + 1
            #To avoid counting same element again  
            freq[j] = -1 
              
    if(freq[i] != -1):  
        freq[i] = count
l=[]
print(freq)  
#Displays the frequency of each element present in array   
for i in range(len(freq)):  
    if(freq[i] != -1 and freq[i]>1):  
        l.append(freq[i])
print(len(l))