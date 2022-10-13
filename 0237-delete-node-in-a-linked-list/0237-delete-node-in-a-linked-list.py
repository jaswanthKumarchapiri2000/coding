# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        nodenext=node.next
        node.val=nodenext.val
        node.next=nodenext.next
        
        
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        