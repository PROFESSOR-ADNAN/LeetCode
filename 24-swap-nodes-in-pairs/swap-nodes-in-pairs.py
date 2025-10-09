# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nodes = []
        cur = head
        while cur:
            nodes.append(cur.val)
            cur = cur.next
        print(nodes)

        for i in range(1, len(nodes), 2):
            nodes[i], nodes[i-1] = nodes[i-1], nodes[i]
        print(nodes)

        dummy = ListNode(0, head)
        res = dummy

        for node in nodes:
            res.next = ListNode(node)
            res = res.next

        return dummy.next