# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDiameterBinaryTree(self, node, diameter) -> int:
        if node is None:
            return 0
        
        lst = self.getDiameterBinaryTree(node.left, diameter)
        rst = self.getDiameterBinaryTree(node.right, diameter)
        print("LST + RST: (val)", lst + rst, node.val)
        diameter[0] = max(lst + rst, diameter[0])
        return 1 + max(lst, rst)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [-1]
        self.getDiameterBinaryTree(root, diameter)
        return diameter[0]