'''
=> DFS
Preorder Traversal
      3
	 / \
	9  20
	  /  \
	 15   7
Note in preorder traversal, for each left subtree or right subtree, it will end with two '##' in the serialized string
Preorder Serialization ['3', '9', '#', '#', '20', '15', '#', '#', '7', '#', '#']
'''
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return ['#']
            
        return [str(root.val)] + self.serialize(root.left) + self.serialize(root.right)
            
    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        print(data)
        ch = data.pop(0)
        if ch == '#':
            return None
            
        root = TreeNode(int(ch))
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        
        return root
