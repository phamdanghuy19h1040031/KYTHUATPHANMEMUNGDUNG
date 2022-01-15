def KT(arr):
    count=0
    for i in arr:
        if type(i)==int:
            if(i<2):
                count=count+1
            else:
                for j in range (2,i-1):
                    if(i%j==0 and j<i):
                        count+=1
                        break
        else:
            count+=1        
    if len(arr)-count >= 2:
        return True
    else:
        return False

a=[6,8,5,10]
print(KT(a))