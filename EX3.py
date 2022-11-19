def insertion(array):
    x = len(array)
    for i in range(x):
        for j in range(0,x):
            if array[i] < array[j]:
                val = array[i]
                array[i] = array[j]
                array[j] = val

array = [10,9,8,7,6,1,3,4,5,2]

print("insertion Array is : ",array)
insertion(array)
print("insertion Array is : ",array)