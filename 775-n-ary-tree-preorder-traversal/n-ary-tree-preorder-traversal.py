"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        def preorder(root):
            if not root:
                return
            if root:
                ans.append(root.val)

            for node in root.children:
                preorder(node)

            return ans

        return preorder(root)