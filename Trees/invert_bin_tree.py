#Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left is not None:
            Solution().invertTree(root.left)
        if root.right is not None:
            Solution().invertTree(root.right)
        return root
