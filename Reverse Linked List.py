# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node= None
        curr= head
        while (curr is not None):
            next= curr.next
            curr.next  = prev_node
            prev_node = curr
            curr = next
        head = prev_node
        return head
