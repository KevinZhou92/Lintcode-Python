'''
=> BFS
Time: O(logn) worst O(n)
Space: O(n)
'''
class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        from collections import deque
        if not root:
            return []
        
        queue = deque([])
        reverse_order = False
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level_nodes = []
            for i in range(size):
                cur_root = queue.popleft()
                level_nodes.append(cur_root.val)
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
            if reverse_order:
                level_nodes = level_nodes[::-1]
            reverse_order = not reverse_order
            res.append(level_nodes)
            
        return res
                    
        
