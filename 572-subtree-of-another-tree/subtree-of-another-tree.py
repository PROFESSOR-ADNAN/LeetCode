# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # def isSame(p, q):
        #     if not p and not q:
        #         return True
        #     if not p or not q or p.val != q.val:
        #         return False

        #     return (isSame(p.left, q.left) and isSame(p.right, q.right))

        # if not root:
        #     return False

        # if isSame(root, subRoot):
        #     return True

        # return isSame(root.left, subRoot) or isSame(root.right, subRoot)

        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return (sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right))
            return False

        if not subRoot: return True
        if not root: return False

        if sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))