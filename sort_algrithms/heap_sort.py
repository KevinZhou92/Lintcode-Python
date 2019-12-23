def heap_sort(nums):
    for i in range((len(nums) - 1) // 2, -1, -1):
        max_heapify(nums, i, len(nums) - 1)

    for i in range(len(nums) - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        max_heapify(nums, 0, i - 1)
    
    return nums

def max_heapify(nums, start, end):
    parent = start
    while 2 * parent + 1 <= end:
        left = 2 * parent + 1
        right = left + 1
        next = parent
        if left <= end and nums[left] > nums[parent]:
            next = left
        if right <= end and nums[right] > nums[next]:
            next = right
        
        if next == parent:
            break

        nums[parent], nums[next] = nums[next], nums[parent]
        parent = next

nums = [1, 3, 2, 6, 5]
print(heap_sort(nums))