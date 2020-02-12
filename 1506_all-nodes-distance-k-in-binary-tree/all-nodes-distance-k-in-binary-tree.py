'''
=> BFS

Time: O(n)
Space: O(n)
'''
from util_class import TreeNode
from collections import deque
class Solution:
    """
    @param root: the root of the tree
    @param target: the target
    @param K: the given K
    @return: All Nodes Distance K in Binary Tree
    """
    def distanceK(self, root, target, K):
        # Write your code here
        if not root:
            return []
        
        if K == 0:
            return [target.val]
            
        def dfs(root, parent):
            if not root:
                return
            root.parent = parent
            dfs(root.left, root)
            dfs(root.right, root)
            
        dfs(root, None)
        queue = deque([target])
        visited = set()
        steps = 0
        res = []
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if steps == K and cur != target:
                    res.append(cur.val)
                for neighbor in [cur.left, cur.right, cur.parent]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            steps += 1
        
        return res