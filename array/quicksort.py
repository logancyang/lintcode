# quicksort

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p)
        quicksort(A, p + 1, hi)

def partition(A, lo, hi):
    pivot = A[lo]
    i = lo
    j = hi
    while True:
        while A[j] > pivot:
            j -= 1
        while A[i] < pivot:
            i += 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j

A = [1, 3, 2, 4]
print A
quicksort(A, 0, 3)
print A
