'''
Space: O(n)
'''
class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        visited = set()
        
        while head:
            if not head in visited:
                visited.add(head)
            else:
                return True
            head = head.next
            
        return False