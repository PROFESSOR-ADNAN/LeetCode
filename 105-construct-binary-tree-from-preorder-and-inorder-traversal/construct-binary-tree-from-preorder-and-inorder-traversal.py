# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # def construct(preorder, inorder):
        #     print(preorder)
        #     print(inorder)
        #     if not preorder or not inorder:
        #         return None

        #     curr = preorder[0]
        #     node = TreeNode(curr)

        #     idx = inorder.index(curr)

        #     node.left = construct(preorder[1:], inorder[:idx])
        #     node.right = construct(preorder[2:], inorder[idx+1:])

        #     return node

        # return construct(preorder, inorder)

        # def constructor(preorder, inorder):
        #     if not inorder:
        #         return None

        #     curr = preorder[0]
        #     node = TreeNode(curr)

        #     idx = inorder.index(curr)
            
        #     newLeftPreorder = []
        #     if len(preorder) > 1:
        #         newLeftPreorder.append(preorder[1])
        #     newLeftPreorder.extend(preorder[3:])
        #     node.left = constructor(newLeftPreorder, inorder[:idx])
        #     node.right = constructor(preorder[2:], inorder[idx+1:])

        #     return node

        # return constructor(preorder, inorder)

        preorder = deque(preorder)

        def build(preorder, inorder):
            if inorder:
                idx = inorder.index(preorder.popleft())
                node = TreeNode(inorder[idx])

                node.left = build(preorder, inorder[:idx])
                node.right = build(preorder, inorder[idx+1:])

                return node

        return build(preorder, inorder)