# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
            
        left = root.left
        right = root.right

        if left and left.val >= root.val:
            return False
        
        if right and right.val <= root.val:
            return False
        
        return True

        return (self.isValidBST(root.left) and self.isValidBST(root.left) )