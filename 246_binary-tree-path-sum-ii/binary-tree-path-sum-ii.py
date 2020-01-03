'''
=> DFS
Remember to backtrack!!!!!!
'''
class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        res = []
        self.traverse(root, target, 0, [], res)
        
        return res
        
    def traverse(self, root, target, level, path, res):
        if not root:
            return
        
        path.append(root.val)
        tmp_target = target
        for i in range(level, -1, -1):
            tmp_target -= path[i]
            if tmp_target == 0:
                tmp = []
                for j in range(i, level + 1):
                    tmp.append(path[j])
                res.append(tmp)
        
        self.traverse(root.left, target, level + 1, path, res)
        self.traverse(root.right, target, level + 1, path, res)
        # !!!!!!!!!!!! Always remember to backtrack in dfs
        path.pop()
        
        