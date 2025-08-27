# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)
        return arr
