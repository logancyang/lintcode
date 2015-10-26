# mergeSort

def mergesort(A):
    # base case
    if len(A) == 0 or len(A) == 1:
        return A

    mid = len(A)/2
    left = mergesort(A[:mid])
    right = mergesort(A[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    ind1 = 0
    ind2 = 0
    while ind1 < len(left) and ind2 < len(right):
        if left[ind1] < right[ind2]:
            result.append(left[ind1])
            ind1 += 1
        else:
            result.append(right[ind2])
            ind2 += 1

    if ind1 < len(left):
        result.extend(left[ind1:])
    if ind2 < len(right):
        result.extend(right[ind2:])
    return result

A = [1, 4, 3, 2, 9]
print mergesort(A)