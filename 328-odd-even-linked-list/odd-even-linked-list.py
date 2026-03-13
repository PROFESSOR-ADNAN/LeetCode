# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode()

        # list1 = head
        # list2 = head.next
        # list3 = dummy

        # while list1.next:
        #     list3.next = list1
        #     list3 = list3.next

        #     list1 = list1.next.next

        # if list1: 
        #     list3.next = list1
        #     list3 = list3.next

        # while list2:
        #     list3 = list2
        #     if list3.next: list3 = list3.next

        #     if list2.next: list2 = list2.next.next
        #     else: break

        # # if list2:
        # #     list3.next = list2

        # return dummy.next

        # if not head: return None

        # dummy = ListNode()

        # list1 = head
        # list2 = head.next
        # list3 = dummy

        # while list1 and list1.next:
        #     list3.next = ListNode(list1.val)
        #     list3 = list3.next

        #     list1 = list1.next.next
        
        # if list1:
        #     list3.next = ListNode(list1.val)
        #     list3 = list3.next

        # while list2 and list2.next:
        #     list3.next = ListNode(list2.val)
        #     list3 = list3.next

        #     list2 = list2.next.next

        # if list2:
        #     list3.next = ListNode(list2.val)
        #     list3 = list3.next

        # return dummy.next
        if not head: return None

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head
