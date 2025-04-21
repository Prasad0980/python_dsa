# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next 
            slow = slow.next
        if fast.next:
            fast = fast.next
            slow = slow.next
        temp = slow.next
        slow.next = None 
        while temp:
            c = temp.next
            temp.next = slow
            slow = temp 
            temp = c 
        while slow.next:
            if slow.val == head.val:
                slow = slow.next
                head = head.next
            else:
                return False
        return True
n4 = ListNode(5)
n3 = ListNode(2, n4)
n2 = ListNode(2,n3)
n1 = ListNode(1,n2)

s = Solution()
print(s.isPalindrome(n1))
        