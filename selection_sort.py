# li = [56,3,2,78,6,0]
# min_val = min(li)
# print(min_val)
# i = li.index(min_val)
# print(i)
# li[0],li[i] = li[i],li[0]
# print(li)


list1 = [56,3,2,78,6,0]
print (list1)
for i in range (len (list1)) :
    min_val = min (list1[i:])
    min_ind = list1. index (min_val)
    list1[i], list1[min_ind] = list1[min_ind],list1[i]
print (list1)