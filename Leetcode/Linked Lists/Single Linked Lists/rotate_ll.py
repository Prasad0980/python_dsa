# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        l = 1
        tail = move = head
        while tail.next:
            tail = tail.next
            l += 1
        k = k % l
        n = l - k
        tail.next = head
        for _ in range(n-1):
            move = move.next
        ret = move.next
        move.next = None
        return ret
