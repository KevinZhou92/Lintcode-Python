from util_class import ListNode
class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        dummy = ListNode(0)
       
        dummy.next = head
        head = dummy
        cur, tail = head.next, head
        duplicate = False
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur = cur.next
                duplicate = True
            else:
                if not duplicate:
                    tail = cur
                else:
                    tail.next = cur.next
                    duplicate = False
                cur = cur.next
        
        return dummy.next
                