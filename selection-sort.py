import random

test_arr = []
random.seed(1234)
for i in range(0,100):
    test_arr.append(int(random.random()*1000))

print(test_arr)


# Insertion Sort

def swap (arr , index):
    stored_num = arr[index-1]
    arr[index-1] = arr[index]
    arr[index] = stored_num

def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            print("i: " + str(i) + " j: " + str(j) + " arr[j]: " + str(arr[j]) + " arr[j-1]: " + str(arr[j-1]))
            swap(arr, j)
            j -= 1
    return arr



print(insertion_sort(test_arr))
