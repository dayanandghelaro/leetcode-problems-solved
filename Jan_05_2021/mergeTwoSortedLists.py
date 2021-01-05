# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_ = []
        while l1:
            list_.append(l1.val)
            l1 = l1.next
        while l2:
            list_.append(l2.val)
            l2 = l2.next
        list_.sort()
        if len(list_) == 0:
            return None
        else:
            node = ListNode(list_[0])
            currentNode = node
            for i in range(1, len(list_)):
                newNode = ListNode(list_[i])
                currentNode.next = newNode
                currentNode = newNode
            return node
        return list_
