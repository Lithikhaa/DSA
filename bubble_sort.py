
def sorted_array(arr):
    arr = [5,2,1,7,4]
    
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
            
arr = [5,2,1,7,4]
sort = sorted_array(arr)    
print(sort)    

