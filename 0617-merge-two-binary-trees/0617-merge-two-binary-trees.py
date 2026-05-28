# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        q=deque([(root1,root2)])
        while q:
            n,m=q.popleft()
            n.val+=m.val
            if m.left and n.left:
                q.append((n.left,m.left))
            elif not n.left:
                n.left=m.left
            if n.right and m.right:
                q.append((n.right,m.right))
            elif not n.right:
                n.right=m.right
        return root1