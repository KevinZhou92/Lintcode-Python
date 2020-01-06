"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not head:
            return head
            
        nodes = []
        while head:
            nodes.append(head)
            tmp = head.next
            head.next = None
            head = tmp
            
        self.quick_sort(nodes, 0, len(nodes) - 1)
        
        dummy = ListNode(0)
        head = dummy
        
        for node in nodes:
            head.next = node
            head = head.next
            
        return dummy.next
        
    def quick_sort(self, nums, start, end):
        if start >= end:
            return 
        
        mid = start + (end - start) // 2
        pivot = nums[mid]
        l, r = start, end
        
        while l <= r:
            while l <= r and nums[l].val < pivot.val:
                l += 1
                
            while l <= r and nums[r].val > pivot.val:
                r -= 1
            
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                
                
        self.quick_sort(nums, start, r)
        self.quick_sort(nums, l, end)

    def merge_sort(self, nums, start, end, tmp):
        if start >= end:
            return 
        
        mid = start + (end - start) // 2
        self.merge_sort(nums, start, mid, tmp)
        self.merge_sort(nums, mid + 1, end, tmp)
        self.merge(nums, start, mid, end, tmp)
        
    def merge(self, nums, start, mid, end, tmp):
        l, r = start, mid + 1
        
        index = start
        while l <= mid and r <= end:
            if nums[l].val < nums[r].val:
                tmp[index] = nums[l]
                l += 1
            else:
                tmp[index] = nums[r]
                r += 1
            index += 1
            
        while l <= mid:
            tmp[index] = nums[l]
            l += 1
            index += 1
            
        while r <= end:
            tmp[index] = nums[r]
            r += 1
            index += 1
            
        for i in range(start, end + 1):
            nums[i] = tmp[i]
        
        
