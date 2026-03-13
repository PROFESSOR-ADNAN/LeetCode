# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # curr = node
        # nxt = node.next

        # while nxt.next:
        #     curr.val = nxt.val
        #     curr = nxt
        #     nxt = nxt.next

        # curr.val = nxt.val
        # curr.next = None

        curr = node
        nxt = node.next

        curr.val = nxt.val
        curr.next = nxt.next

        nxt.next = None
        del nxt