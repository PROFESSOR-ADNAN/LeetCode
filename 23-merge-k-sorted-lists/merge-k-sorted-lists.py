# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            n = len(lists)
            curr_merged_list = []
            for i in range(0, n, 2):
                if i+1 < n:
                    curr_merged_list.append(self.merge_linked_list(lists[i], lists[i+1]))
                else:
                    curr_merged_list.append(lists[i])

            lists = curr_merged_list

        return lists[0]

    def merge_linked_list(self, list1, list2):
        dummy = ListNode()
        list3 = dummy

        while list1 and list2:
            if list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next

            list3 = list3.next

        if list1:
            list3.next = list1
            list3 = list3.next
        if list2:
            list3.next = list2
            list3 = list3.next

        return dummy.next






            
