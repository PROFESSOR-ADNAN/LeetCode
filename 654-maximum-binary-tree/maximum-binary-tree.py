# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # mx = max(nums)
        # idx = nums.index(mx)

        # left = nums[0:idx]
        # right = nums[idx+1:]

        # left.sort(reverse=True)
        # right.sort(reverse=True)

        # root = TreeNode(mx)

        # curr = root
        # for val in left:
        #     treeNode = TreeNode(val)

        #     curr.left = treeNode
        #     curr = treeNode

        # curr = root
        # for val in right:
        #     treeNode = TreeNode(val)

        #     curr.right = treeNode
        #     curr = treeNode

        # return root

        if not nums:
            return

        mx = max(nums)
        idx = nums.index(mx)

        node = TreeNode(mx)

        node.left = self.constructMaximumBinaryTree(nums[0:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx+1:])

        return node

