# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # if headA is headB:
        #     return headA
        # temp_a, temp_b = headA, headB
        # while temp_a.next and temp_b.next:
        #     temp_a = temp_a.next
        #     temp_b = temp_b.next 
        #     if temp_a is temp_b:
        #         return temp_a 
        # count = 0
        # if temp_a.next: 
        #     while temp_a.next:
        #         temp_a = temp_a.next 
        #         count +=1 
        #     for _ in range(count):
        #         headA = headA.next
        # else:
        #     while temp_b.next:
        #         temp_b = temp_b.next
        #         count +=1 
        #     for _ in range(count):
        #         headB = headB.next 
        # if headA is headB:
        #     return headA
        # while headA and headB:
        #     headA = headA.next
        #     headB = headB.next
        #     if headA is headB:
        #         return headA 
        # else:
        #     return None 
        # # one = headA
        # # two = headB

        # # while one != two:
        # #     one = headB if one is None else one.next
        # #     two = headA if two is None else two.next
        # # return one

        tempa = headA
        tempb = headB

        while tempa is not tempb:
            tempa = headB if not tempa else tempa.next
            tempb = headA if not tempb else tempb.next
        return tempa

        
        
        
        