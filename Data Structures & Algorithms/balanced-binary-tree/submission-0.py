# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkIfBalanced(self, node):
        if node is None:
            return 0
        
        lsh = self.checkIfBalanced(node.left)
        if lsh is False:
            return lsh
        rsh = self.checkIfBalanced(node.right)
        if rsh is False:
            return rsh

        if abs(lsh - rsh) > 1:
            return False
        return 1 + max(lsh, rsh)

        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isTreeBalanced = self.checkIfBalanced(root)
        if isTreeBalanced is False:
            return False
        else:
            return True
