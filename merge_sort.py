
def sorted_arr(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    left = sorted_arr(left)
    right = sorted_arr(right)
    
    
    return merge(left,right)

    

def merge(low,high):
    merge = []
    low_index,high_index = 0,0
    while low_index < len(low) and high_index < len(high):
        if low[low_index] < high[high_index]:
            merge.append(low[low_index])
            low_index += 1
        else:
            merge.append(high[high_index])
            high_index += 1
    while low_index < len(low):
            merge.append(low[low_index])
            low_index += 1
    while high_index < len(high):
            merge.append(high[high_index])
            high_index += 1
    return merge
    
        
        

arr = [12,11,13,6,5,7]
sort = sorted_arr(arr) 
print(sort)   

