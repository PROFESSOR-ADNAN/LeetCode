# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # stack = []
        # curr = head

        # while curr:
        #     while stack and stack[-1] < curr.val:
        #         stack.pop()

        #     stack.append(curr.val)
        #     curr = curr.next

        # dummy = ListNode()
        # curr = dummy

        # for val in stack:
        #     newNode = ListNode(val)
        #     curr.next = newNode
        #     curr = curr.next

        # return dummy.next


        def reverse(head):
            prev, curr = None, head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        # newHead = reverse(head)
        # mx = 0

        # dummy = ListNode()
        # ans = dummy
        # curr = newHead

        # while curr:
        #     if curr.val >= mx:
        #         ans.next = curr
        #         ans = ans.next
        #         mx = max(mx, curr.val)

        #     curr = curr.next

        # ans.next = None
        # return reverse(dummy.next)

        head = reverse(head)
        curr = head
        curr_max = curr.val

        while curr.next:
            if curr.next.val < curr_max:
                curr.next = curr.next.next
            else:
                curr_max = curr.next.val
                curr = curr.next

        return reverse(head)