# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow = head
        fast = head.next
        while fast:
            temp = fast.next
            fast.next = slow
            if slow == head:
                slow.next = None
            slow = fast
            fast = temp
        return slow
    
n3 = ListNode(0)
n2 = ListNode(1, n3)
n1 = ListNode(2, n2)

s = Solution()  
op = s.reverseList(n1)
print(op.val, op.next.val, op.next.next.val)
