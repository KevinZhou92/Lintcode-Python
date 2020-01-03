
def sortIntegers(A):
    quick_sort(A, 0, A.length-1)

def quick_sort(A, start, end):
    if start >= end:
        return
    
    pivot_index = partition(A, start, end)
    quick_sort(A, start, pivot_index-1)
    quick_sort(A, pivot_index+1, end)

def partition(A, start, end) {
    pivot_index = start+(end-start)/2
    pivot = A[pivot_index]
    
    // swap A[start] and A[pivot_index]
    t = A[start]
    A[start] = A[pivot_index]
    A[pivot_index] = t
    
    // partition A[start+1...end] so that A[start+1...r] <= pivot and A[l...end] >= pivot  
    l, r = start + 1, end;
    while (l <= r) {
        while (l <= r and A[l] < pivot:
            l += 1
        while l <= r and A[r] > pivot
            r -= 1
        if l <= r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1

    
    // swap pivot and A[r
    A[start] = A[r]
    A[r] = pivot

    return r

