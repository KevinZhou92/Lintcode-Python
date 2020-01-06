from util_class import RandomListNode
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return None
        
        node_map = {}
        dummy = ListNode(0)
        tail = dummy
        cur = head
        while cur:
            new_node = RandomListNode(cur.label)
            tail.next = new_node
            tail = tail.next
            node_map[cur] = new_node
            cur = cur.next
            
        while head:
            if head.random:
                new_random_next = node_map[head.random]
                new_head = node_map[head]
                new_head.random = new_random_next
            head = head.next
            
        return dummy.next
            