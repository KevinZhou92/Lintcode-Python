from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if not root:
            return []
            
        queue = deque([])
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
            res.append(level_nodes)
            
        return res