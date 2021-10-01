import time
  
start = time.time()
count = 0
with open("read.txt") as file:
    for line in file:
        lis=list(line)
        for item in lis:
            if ord(item.upper())>=ord('A') and ord(item.upper())<=ord('Z'):
                count+=1
end =  time.time()
print("Execution time in seconds: ",(end-start))
print("No of lines printed: ",count)