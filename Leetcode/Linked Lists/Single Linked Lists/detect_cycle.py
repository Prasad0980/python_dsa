# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                break
        else:
            return None
        # while head is not slow:
        #     head = head.next
        #     slow = slow.next
        # return slow
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
