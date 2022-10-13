# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        slow,fast=head,head
        while( (fast.next) and fast.next.next!=None):
            fast=fast.next.next
            slow=slow.next
        if fast.next :
            slow.next=slow.next.next
        else:
            slow.val=slow.next.val
            slow.next=slow.next.next
        return head
        