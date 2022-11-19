def selection(array):
    x = len(array)
    for i in range(x):
        for j in range(i+1,x):
            if array[i] > array[j]:
                val = array[i]
                array[i] = array[j]
                array[j] = val

array = [10,9,8,7,6,1,3,4,5,2]

print("selection Array is : ",array)
selection(array)
print("selection Array is : ",array)