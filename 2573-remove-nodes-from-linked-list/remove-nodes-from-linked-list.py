# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head

        while curr:
            while stack and stack[-1] < curr.val:
                stack.pop()

            stack.append(curr.val)
            curr = curr.next

        print(stack)

        dummy = ListNode()
        curr = dummy

        for val in stack:
            newNode = ListNode(val)
            curr.next = newNode
            curr = curr.next

        return dummy.next
