# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        ptr = result

        carry = 0 
        n1 = l1
        n2 = l2

        while n1 or n2 is not None:
            sum = 0 + carry

            if n1 is not None:
                sum += n1.val
                n1 = n1.next
            if  n2 is not None:
                sum += n2.val
                n2 = n2.next

            carry = sum // 10
            sum = sum % 10

            ptr.next = ListNode(sum)
            ptr = ptr.next
        if carry != 0:
            ptr.next = ListNode(carry)
        return result.next