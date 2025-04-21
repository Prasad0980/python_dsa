# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow, fast = head, head.next
        while fast:
            if slow.val != fast.val:
                slow.next = fast
                slow = fast
            fast = fast.next
        slow.next = None
        return head
