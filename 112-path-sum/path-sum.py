# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        sm = 0
        def path(node):
            nonlocal sm
            if not node:
                return
            if not node.left and not node.right:
                sm += node.val
                if sm == targetSum:
                    return True
                sm -= node.val
                return

            sm += node.val

            if path(node.left):
                return True

            if path(node.right):
                return True

            sm -= node.val

        if path(root):
            return True
        
        return False