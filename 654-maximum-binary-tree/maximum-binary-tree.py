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

        # if not nums:
        #     return

        # mx = max(nums)
        # idx = nums.index(mx)

        # node = TreeNode(mx)

        # node.left = self.constructMaximumBinaryTree(nums[0:idx])
        # node.right = self.constructMaximumBinaryTree(nums[idx+1:])

        # return node



        # n = len(nums)

        # def constructor(left, right):
        #     if left > right:
        #         return None

        #     mxIdx = left
        #     for i in range(left, right+1):
        #         if nums[i] > nums[mxIdx]:
        #             mxIdx = i

        #     left_node = constructor(left, mxIdx-1)
        #     right_node = constructor(mxIdx+1, right)

        #     return TreeNode(nums[mxIdx], left_node, right_node)

        # return constructor(0, n-1)

        n = len(nums)

        def constructor(left, right):
            if left > right:
                return None

            mxIdx = left
            for i in range(left, right+1):
                if nums[i] > nums[mxIdx]:
                    mxIdx = i
            
            node = TreeNode(nums[mxIdx])

            node.left = constructor(left, mxIdx-1)
            node.right = constructor(mxIdx+1, right)

            return node

        return constructor(0, n-1)