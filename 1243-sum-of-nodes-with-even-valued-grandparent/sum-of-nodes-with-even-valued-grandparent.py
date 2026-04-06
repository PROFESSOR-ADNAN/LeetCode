# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        # ans = []
        # def bfs():
        #     q = deque([root])
            
        #     while q:
        #         temp = []
        #         for i in range(len(q)):
        #             node = q.popleft()
        #             if node:
        #                 temp.append(node.val)
        #             else:
        #                 temp.append(0)
        #             if node:
        #                 q.append(node.left)
        #                 q.append(node.right)

        #         ans.append(temp)

        # bfs()
        # # print(*ans)

        # grandParent = defaultdict(int)
        # for i in range(2, len(ans)-1):
        #     prev = ans[i-2]
        #     curr = ans[i]
        #     # print(prev, curr)

        #     ind = 0
        #     for i in range(0, len(curr), 4):
        #         a, b, c, d = curr[i], curr[i+1], curr[i+2], curr[i+3]

        #         # print(a, b, c, d)

        #         # grandParent[a] = prev[ind]
        #         # grandParent[b] = prev[ind]
        #         # grandParent[c] = prev[ind]
        #         # grandParent[d] = prev[ind]

        #         grandParent[prev[ind]] = [a, b, c, d]

        #         ind += 1

        # # print(grandParent)

        # answer = 0
        # for grandParent, childs in grandParent.items():
        #     # print(grandParent, childs)
        #     if grandParent % 2 == 0:
        #         answer += sum(childs)

        # return answer

        def getSubTreeSum(currNode, parentVal, grandParentVal):
            sum =  0
            if (grandParentVal % 2 == 0):
                sum += currNode.val

            left_sum = 0
            if currNode.left:
                left_sum = getSubTreeSum(currNode.left, currNode.val, parentVal)

            right_sum = 0
            if currNode.right:
                right_sum = getSubTreeSum(currNode.right, currNode.val, parentVal)

            return sum + left_sum + right_sum

        return getSubTreeSum(root, -1, -1)