# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        path = []

        def allPath(node):
            nonlocal path, ans
            if not node:
                return

            if not node.left and not node.right:
                path.append(node.val)
                if sum(path) == targetSum:
                    ans.append(path[:])

                path.pop()
                return

            path.append(node.val)
            allPath(node.left)
            allPath(node.right)

            path.pop()

        allPath(root)
        return ans