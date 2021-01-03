# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        elements = []
        for list_ in lists:
            curr_list = list_
            while curr_list is not None:
                elements.append(curr_list.val)
                curr_list = curr_list.next
        elements.sort()
        if len(elements) > 0:
            newList = ListNode(elements[0])
            cur_list = newList
            for i in range(1, len(elements)):
                adList = ListNode(elements[i])
                cur_list.next = adList
                cur_list = adList
            return newList
        else:
            return None
