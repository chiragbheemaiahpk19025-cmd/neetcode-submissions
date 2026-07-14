# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMaxDepth(self, node) -> int:
        if node is None:
            return 0
        lsh = self.getMaxDepth(node.left)
        rsh = self.getMaxDepth(node.right)
        return 1 + max(lsh, rsh)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDepth(root)