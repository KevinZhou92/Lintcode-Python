def merge_sort(nums):
    tmp_array = [0] * (len(nums))
    mergesort(nums, 0, len(nums) - 1, tmp_array)

    return nums

def mergesort(nums, start, end, tmp_array):
    if start >= end:
        return
    
    mid = start + (end - start) // 2
    mergesort(nums, start, mid, tmp_array)
    mergesort(nums, mid + 1, end, tmp_array)
    merge(nums, start, mid, end, tmp_array)

def merge(nums, start, mid, end, tmp_array):
    l, r = start, mid + 1
    index = start
    while l <= mid and r <= end:
        if nums[l] < nums[r]:
            tmp_array[index] = nums[l]
            l += 1
        else:
            tmp_array[index] = nums[r]
            r += 1
        index += 1

    while l <= mid:
        tmp_array[index] = nums[l]
        l += 1
        index += 1

    while r <= end:
        tmp_array[index] = nums[r]
        r += 1
        index += 1

    for i in range(start, end + 1):
        nums[i] = tmp_array[i]

nums = [2,3,7,6,1]
print(merge_sort(nums))