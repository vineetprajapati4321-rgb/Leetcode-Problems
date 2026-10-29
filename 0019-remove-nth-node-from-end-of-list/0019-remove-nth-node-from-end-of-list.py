# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next

        p = l - n + 1
        # when head needs to be deleted
        if p == 1:
            return head.next

        # Reach the node before target
        temp = head
        for i in range(p - 2):
            if temp.next == None:
                return head
            temp = temp.next

        temp.next = temp.next.next

        return head
