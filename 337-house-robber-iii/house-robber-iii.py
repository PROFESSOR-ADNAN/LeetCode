# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # q = deque([root])

        # sm = []
        # while q:
        #     n = len(q)
        #     total = 0
        #     for _ in range(n):
        #         curr = q.popleft()
        #         total += curr.val

        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)

        #     sm.append(total)

        # print(sm)

        # if len(sm) == 1: return sm[0]

        # dp = [0] * len(sm)
        # dp[0] = sm[0]
        # dp[1] = max(dp[0], sm[1])

        # for i in range(2, len(sm)):
        #     dp[i] = max(dp[i-2] + sm[i], dp[i-1])

        # return dp[-1]
        


        def dfs(node):
            if not node:
                return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            rob_current = node.val + left[1] + right[1]

            not_rob_current = max(left[0], left[1]) + max(right[0], right[1])
            
            return [rob_current, not_rob_current]

        ans = dfs(root)
        res = max(ans[0], ans[1])

        return res