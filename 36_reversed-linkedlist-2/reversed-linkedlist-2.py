"""
Input: 1->2->3->4->5->NULL, m = 2 and n = 4, 
Output: 1->4->3->2->5->NULL.

we need to get the node in front of node and the node past 
connect the prev_m_node with n_node
connect m node with post_n_node
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
        for _ in range(m - 1):
            head = head.next
        
        prev_m_node = head
        m_node = prev_m_node.next
        # head
        n_node = m_node
        # tail
        post_n_node = n_node.next
        
        for i in range(n - m):
            tmp = post_n_node.next
            post_n_node.next = n_node
            n_node = post_n_node
            post_n_node = tmp
            
        prev_m_node.next = n_node
        m_node.next = post_n_node
        
        
        return dummy.next
