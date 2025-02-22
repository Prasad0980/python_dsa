from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head and head.next):
            return head
        dummy = slow = ListNode(-1, head)
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next 
            else:
                slow.next = head
                slow = head 
            head = head.next
        slow.next = head 
        return dummy.next