def binary_search(nums, target):
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] <= end:
            start = mid
        else:
            end = mid
    
    if nums[end] == target:
        return end
    
    if nums[start] == target:
        return start

    return -1

def find_first_last_index(nums, target):
        first_index = -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
                
        if nums[start] == target:
            first_index = start
        elif nums[end] == target:
            first_index = end
        
        last_index = -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        
        if nums[end] == target:
            last_index = end
        elif nums[start] == target:
            last_index = start
        
        return [first_index, last_index]

def search_insert_position(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
                
        if nums[start] >= target:
            return 0
            
        if nums[end] < target:
            return end + 1
        
        return end