"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = b = root
        x = []
        y = []
        if p == root or q == root:
            return root
        while a != p:
            x.append(a)
            if a.val > p.val:
                a = a.left
            elif a.val < p.val:
                a = a.right    
            if a.val == p.val and a.val not in x:
                x.append(a)
        if q.val in x:
            return q
        while b != q:
            y.append(b)
            if b.val > q.val:
                b = b.left
            elif b.val < q.val:
                b = b.right    
            if b.val == b.val and b.val not in y:
                y.append(b)
        first = next((t for t in reversed(x) if t in reversed(y)), None)
        return first
