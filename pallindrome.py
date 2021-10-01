s="mom you have a kayak"
l=list(s.split(" "))
def palindrome(str):
    if str==str[::-1]:
        return True
    else:
        return False

lst2 = sorted(l, key=len)
i=0
j=-1
while(True):
    if palindrome(lst2[i]) and palindrome(lst2[j]):
        print(palindrome(lst2[i]))
        print(palindrome(lst2[j]))
        break
    else:
        i+=1
        j-=1

