# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        n_s = temp = ListNode(-1)
        while l1 and l2:
            print(l1.val)
            print(l2.val)
            rem = (l1.val + l1.val + carry) % 10
            print(rem)
            carry = (l1.val + l2.val + carry)//10
            n_s.next = ListNode(rem)
            n_s = n_s.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            rem = (l1.val + carry) % 10
            carry = (l1.val + carry)//10
            n_s.next = ListNode(rem)
            n_s = n_s.next
            l1 = l1.next
        if l2:
            rem = (l2.val + carry) % 10
            carry = (l2.val + carry)//10
            n_s.next = ListNode(rem)
            n_s = n_s.next
            l2 = l2.next
        if carry > 0:
            n_s.next = ListNode(carry)
        return temp.next

num1_1 = ListNode(3, None)
num1_2 = ListNode(4, num1_1)
num1_3 = ListNode(2, num1_2) 

num2_1 = ListNode(4, None)
num2_2 = ListNode(6, num2_1)
num2_3 = ListNode(5, num2_2)

s= Solution()
print(s.addTwoNumbers(num1_3, num2_3))