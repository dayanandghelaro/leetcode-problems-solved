# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head
        elif head is None:
            return None
        else:
            l = []
            newList = []
            while head:
                l.append(head.val)
                head = head.next
            for i in range(0, len(l), k):
                if i+k <= len(l):
                    ll = l[i:i+k]
                    
                    ll.reverse()
                    newList += ll
                else:
                    newList +=l[i:]
            lis = ListNode(newList[0])
            curP = lis
            for e in newList[1:]:
                newLis = ListNode(e)
                curP.next = newLis
                curP = newLis
            return lis
