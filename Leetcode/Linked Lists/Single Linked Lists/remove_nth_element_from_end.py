# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head 
        for _ in range(n):
            fast = fast.next 
        if not fast:
            return slow.next #This is important for removal of first element.
        while fast.next:
            fast = fast.next
            slow = slow.next
        else:
            slow.next = slow.next.next
        return head 

        