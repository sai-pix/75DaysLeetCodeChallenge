# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p==root or q==root:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        righ=self.lowestCommonAncestor(root.right,p,q)
        if left and righ:
            return root
        return left if left else righ