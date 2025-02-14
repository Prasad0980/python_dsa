# Definition for singly-linked list.
from typing import Optional

"""The highlighted solution is mine. It uses no additional space but has complex edge cases. 
THe below solution is claude ai solution with less complex code but additional node.
What is important is the two ways to reverse any linked list. 
Take example: 1->2->3->4->5
Normal appraoch: None<-1 2->3->4->5, None<-1<-2 3->4->5, None<-1<-2<-3 4->5,None<-1<-2<-3<-4 5, None<-1<-2<-3<-4<-5
Claude approach: 2->1->3->4->5, 3->2->1->4->5, 4->3->2->1->5, 5->4->3->2->1

Although, the approach given by claude is only useful when we have been given the indices"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#         if left == right:
#             return head
#         slow = fast = default = head
#         for i in range(right-1):
#             if i < left-1: 
#                 slow = slow.next 
#             if i < left - 2:
#                 head= head.next
#             fast = fast.next 
#         c = slow.next 
#         slow.next = fast.next
#         while slow is not fast: #we can also use while cache condition here
#             cache = c.next
#             c.next = slow
#             slow = c
#             c = cache
#         if left == 1:
#             return slow
#         else:
#             head.next = slow
#             return default
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Handle edge cases
        if not head or left == right:
            return head
            
        # Dummy node to handle cases where left = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move to the node just before reversal starts
        for _ in range(left - 1):
            prev = prev.next
            
        # Start reversal
        current = prev.next
        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next
            
        