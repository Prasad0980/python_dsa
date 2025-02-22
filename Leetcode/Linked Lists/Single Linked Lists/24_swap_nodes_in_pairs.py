from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while not (head and head.next):
            return head
        s, f = head, head.next
        ret = f
        while f:
            temp = f.next
            s.next = f.next.next if (f.next and f.next.next) else f.next
            f.next = s
            s = temp
            f = s.next if s else None
        return ret

#Concept: Here the main stuff was with regards to odd number of nodes and even number of nodes
# When there are even nodes, it is easy for the slow node to connect to fast.next.next 
#But when there are odd nodes, we need to link the slow node in the last iteration to the slow.next node