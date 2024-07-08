'''insertion sort is especially efficient when it comes to sorting small datasets; 
since fewer elements need to be processed and moved around, this algorithm saves time compared to others.'''
#insertion sort            7 --- sorted 1,4,5,3,2 -- unsorted
arr = [7,1,4,5,3,2]

for i in range(1,len(arr)):            #i -- 1(unsorted) pos > 0 --- for stopping condition
     current = arr[i]
     pos = i
     while current<arr[pos-1] and pos>0:
         arr[pos] = arr[pos-1]
         pos = pos-1
     arr[pos] = current
print(arr)
         