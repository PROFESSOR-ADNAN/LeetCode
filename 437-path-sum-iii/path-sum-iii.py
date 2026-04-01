# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.ans = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # curr = 0
        # ans = 0
        # def allPath(node):
        #     nonlocal curr, ans
        #     if not node:
        #         return

        #     curr += node.val
        #     print(curr)
        #     if curr == targetSum:
        #         ans += 1
        #         curr = 0
        #     elif curr > targetSum:
        #         curr = 0
            
        #     allPath(node.left)
        #     allPath(node.right)

        #     curr -= node.val

        # allPath(root)
        # return ans

        # path = []
        # ans = set()

        # def allPath(node):
        #     nonlocal path, ans
        #     if not node:
        #         return

        #     if not node.left and not node.right:
        #         path.append(node.val)
        #         print(*path)
                
        #         left = 0
        #         curr = 0
        #         for right in range(len(path)):
        #             curr += path[right]
        #             while left <= right and curr > targetSum:
        #                 curr -= path[left]
        #                 left += 1
                    
        #             if path[left:right+1] and curr == targetSum:
        #                 ans.add(tuple(path[left:right+1]))
        #         print(ans)
        #         path.pop()
        #         return

        #     path.append(node.val)
        #     allPath(node.left)
        #     allPath(node.right)

        #     path.pop()

        # allPath(root)
        # return len(ans)

        # def dfs(node, curr):
        #     if not node:
        #         return

        #     if not node.left and not node.right:
        #         curr += node.val
        #         if curr == targetSum:
        #             self.ans += 1
        #         curr -= node.val
        #         return

        #     curr += node.val
        #     if curr == targetSum:
        #         self.ans += 1
        #     dfs(node.left, curr)
        #     dfs(node.right, curr)

        #     curr -= node.val

        # if not root:
        #     return 0

        # dfs(root, 0)

        # self.pathSum(root.left, targetSum)
        # self.pathSum(root.right, targetSum)

        # return self.ans

        self.ans = 0
        self.map = defaultdict(int)
        self.map[0] = 1

        def dfs(node, curr):
            if not node:
                return

            curr += node.val
            self.ans += self.map[curr-targetSum]
            self.map[curr] += 1

            if node.left:
                dfs(node.left, curr)
            if node.right:
                dfs(node.right, curr)

            self.map[curr] -= 1

        dfs(root, 0)
        return self.ans

