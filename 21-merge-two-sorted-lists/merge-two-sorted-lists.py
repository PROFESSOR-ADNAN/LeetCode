# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        tail = dummy 
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next
                












        
        # n = list1
        # arr = []

        # while n is not None:
        #     arr.append(n.val)
        #     n = n.next
        # print(arr)

        # for i in range(len(arr)):
        #     value = arr[i]
        #     if list2 is None:
        #         new_node = ListNode(value)
        #         list2 = new_node
        #     else:
        #         m = list2
        #         while m is not None:
        #             if m.val == value:
        #                 new_node = ListNode(value)
        #                 new_node.next = m.next
        #                 m.next = new_node
        #                 break
        #             elif m.val < value:
        #                 if m.next is None:
        #                     new_node = ListNode(value)
        #                     m.next = new_node
        #                     m = m.next
        #                     break
        #                 prevM = m
        #                 m = m.next
        #             elif m.val > value:
        #                 new_node = ListNode(value)
        #                 new_node.next = prevM.next
        #                 prevM.next = new_node
        #                 break
        # return list2