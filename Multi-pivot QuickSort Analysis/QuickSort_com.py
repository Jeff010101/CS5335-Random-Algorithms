from numpy.random import randint
import time
import random
import numpy as np
import copy

# np.random.seed(10)

global n1, n2, n3
n1, n2, n3 = 0, 0, 0

## CS5335 Experiment: Quicksort

# basic operations

# swap two number at position n, m of array A
def swap(A, n, m):
        temp = A[n]
        A[n] = A[m]
        A[m] = temp

def partition1(A, start, end):
        global n1
        point = start

        for i in range(start,end):
                n1 += 1
                if A[i]<A[end]:
                        swap(A, i, point)
                        point += 1
        swap(A, point, end)
        return point

# 2 pivot partition
def partition2(A, start, end):
        L, K, G = start+1, start+1, end-1
        global n2

        n2 += 1
        if A[start]>A[end]:
                swap(A,start,end)
        while(K<=G):
                n2 += 1
                if A[start]>A[K]:
                        swap(A, K, L)
                        K += 1
                        L += 1
                else:
                        n2 += 1
                        if A[end]>=A[K]:
                                K += 1
                        else:
                                swap(A, K, G)
                                G -= 1
        swap(A, start, L-1)
        swap(A, end, G+1)
        return L-1, G+1

def partition3(A, start, end):
        global n3
        n3 += 1
        if A[start]>A[end]:
                swap(A,start,end)
        n3 += 1
        if A[start+1]>A[end]:
                swap(A,start+1, end)
        n3 += 1
        if A[start]>A[start+1]:
                swap(A,start,start+1)
        a, b, c, d = start+2, start+2, end-1, end-1
        L, M, H = A[start], A[start+1], A[end]
        while(b<=c):
                while(A[b]<M and b<=c):
                        n3 += 1
                        if A[b]<L:
                                swap(A,a,b)
                                a += 1
                        b += 1
                        n3 += 1
                while(A[c]>M and b <= c):
                        n3 += 1
                        if A[c]>H:
                                swap(A,c,d)
                                d -= 1
                        c -= 1
                        n3 += 1
                if b<=c:
                        n3 += 1
                        if A[b]>H:
                                n3 += 1
                                if A[c]<L:
                                        swap(A,b,a)
                                        swap(A,a,c)
                                        a += 1
                                else:
                                        swap(A,b,c)
                                swap(A,c,d)
                                b += 1
                                c -= 1
                                d -= 1
                        else:
                                n3 += 1
                                if A[c]<L:
                                        swap(A,b,a)
                                        swap(A,a,c)
                                        a += 1
                                else:
                                        swap(A,b,c)
                                b += 1
                                c -= 1
        a -= 1
        b -= 1
        c += 1
        d += 1
        swap(A, start+1, a)
        swap(A, a, b)
        a -= 1
        swap(A,start,a)
        swap(A,end,d)
        return a, b, d


        
        



# 1 pivot Quicksort
def quicksort(A, start, end):
        if start<end:
                pivot = partition1(A, start, end)
                quicksort(A, start, pivot-1)
                quicksort(A, pivot+1, end)

# 2 pivots Quicksort
def quicksort2(A, start, end):
        if start<end:
                L, G = partition2(A,start,end)
                quicksort2(A, start, L-1)
                quicksort2(A, L+1, G-1)
                quicksort2(A, G+1, end)


# 3 pivots Quicksort
def quicksort3(A, start, end):
        global n3
        if start+1<end:
                L, M, H = partition3(A,start,end)
                quicksort3(A,start,L-1)
                quicksort3(A,L+1,M-1)
                quicksort3(A,M+1,H-1)
                quicksort3(A,H+1,end)
        else:
                if start<end:
                        n3 += 1
                        if A[start]>A[end]:
                                swap(A,start,end)




## test
def check(A):
        for i in range(0,len(A)-1):
                if A[i]>A[i+1]:
                        return False
        return True
N = 30
time1 = np.zeros(N)
time2 = np.zeros(N)
time3 = np.zeros(N)
for i in range(0,N):
        A = randint(0,10000, size = 10000)
        B = copy.deepcopy(A)
        C = copy.deepcopy(A)
        # start = time.time()
        quicksort(A, 0, len(A)-1)
        # end = time.time()
        # time1[i] = (end - start)
        result1 = check(A)
        # start = time.time()
        quicksort2(B, 0, len(B)-1)
        # end = time.time()
        # time2[i] = (end - start)
        result2 = check(B)
        # start = time.time()
        quicksort3(C, 0, len(C)-1)
        # end = time.time()
        # time3[i] = (end - start)
        result3 = check(C)
print(n1/N,result1)
print(n2/N,result2)
print(n3/N,result3)