def bubble(array):
    x = len(array)
    for i in range(x-1):
        for j in range(0,x-i-1):
            if array[j] > array[j+1]:
                val = array[j]
                array[j] = array[j+1]
                array[j+1] = val

array = [10,9,8,7,6,1,3,4,5,2]

print("Unsort Array is : ",array)
bubble(array)
print("sort Array is : ",array)