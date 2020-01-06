class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addLists2(self, l1, l2):
        # write your code here
        num1 = 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
            
        num2 = 0
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
            
        res = num1 + num2
        if res == 0:
            return ListNode(0)
        
        dummy = ListNode(0)
        while res > 0:
            head = ListNode(res % 10)
            res = res // 10
            head.next = dummy.next
            dummy.next = head
            
        return dummy.next
            
