'''
=> Two-pointer
'''
class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if not head or not head.next:
            return False
            
        slow = head
        fast = head.next
        
        # 1- 2
        # | _|
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
            
        return False