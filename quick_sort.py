
def partions(array,low,high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] <= pivot:
            i = i + 1
            (array[i],array[j]) = (array[j],array[i])
    (array[i+1],array[high]) = (array[high],array[i+1]) 
    return i + 1
            
    
def quicksort(array,low,high):
    if low < high:
        pi = partions(array,low,high)
        quicksort(array,low,pi - 1)
        quicksort(array,pi + 1,high)


if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    n = len(array)
    quicksort(array,0,n-1)
    for x in array:
        print(x, end=" ")
