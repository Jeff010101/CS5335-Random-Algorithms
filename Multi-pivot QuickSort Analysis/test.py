from numpy.random import randint
import time
import numpy as np

np.random.seed(10)

def insert_sort(arr, l, r):
    for i in range(l+1, r+1):
        j = i - 1
        temp = arr[i]
        if arr[i] < arr[j]:
            while j >= 0 and arr[j] > temp:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = temp
 
 
def _partition_doubule(arr, l, r):
    ind = random.randint(l, r)
    arr[l], arr[ind] = arr[ind], arr[l]
    stand = arr[l]
    i, j = l+1, r
    while True:
        while i <= r and arr[i] < stand:    #不能改为arr[i] <= stand, 原因下文有讲解
            i += 1
        while j >= l+1 and arr[j] > stand:  #不能改为arr[j] >= stand.
            j -= 1 
        if i > j:
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    arr[j], arr[l] = arr[l], arr[j]
    return j
 
 
def _quick_sort(arr, l, r):
    if (r - l) < 15:    #当待排序元素个数小于15时改为插入排序，可提高程序运行速度
        insert_sort(arr, l, r)
        return
    p = _partition_doubule(arr, l, r)
    _quick_sort(arr, l, p-1)
    _quick_sort(arr, p+1, r)
 
 
def quick_sort(arr, nums):
    _quick_sort(arr, 0, nums-1)


A = randint(0,1000, size = 100000)
start1 = time.time()
quicksort2(A, 0, len(A)-1)
end1 = time.time()
print(end1 - start1)