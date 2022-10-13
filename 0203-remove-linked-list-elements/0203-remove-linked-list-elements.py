# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(51,head)
        k=val
        cur=dummy
        while((cur.next)!=None):
            while( cur.next and cur.next.val!=k):
                cur=cur.next
            while(cur.next and (cur.next.val)==k):
                cur.next=cur.next.next
                
        return dummy.next
            
        