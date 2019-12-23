def quick_sort(nums):
    quicksort(nums, 0, len(nums) - 1)
    
    return(nums)

def quicksort(nums, start, end):
    if start >= end:
        return 

    mid = start + (end - start) // 2
    pivot = nums[mid]
    l, r = start, end

    while l <= r:
        while l <= r and nums[l] < pivot:
            l += 1
        while l <= r and nums[r] > pivot:
            r -= 1

        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    quicksort(nums, start, r)
    quicksort(nums, l, end)

nums = [2, 7, 9, 1, 3]
print(quick_sort(nums))