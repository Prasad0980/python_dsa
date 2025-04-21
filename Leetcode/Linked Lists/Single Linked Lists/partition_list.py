# Definition for singly-linked list.


#My learnings from this: 
"""In this question, I was given a value. I had to put all the elements less than x before (in the left) and all elements
more than or equal to x in right side and return that linked list. The original order of elements was to be maintained.
So let's say if i am give 5-6-2-3-1-0-8-2 with x as 3, I am supposed to return 2-1-0-2-5-6-3-8.
Now the logic I derived was this: this final list is basically combination of two smaller lists. One list on left
with all elements less than x and other on right with all elements more than x. 
So all I had to do was to join the elements smaller together and larger ones together. For that what was important for 
me was to find the first appearance of small and big. Because I would use them as refernce to join them to next ones.
Like in above example, I find that 6 is the bigger which would be joined to next bigger and 2 is the smaller which would 
be used to join smaller. Once I find 6, while iterating across, I will join it to 3 and then join 3 to 8 and so on.
Similarly, I will join 2 to 1, 1 to 0 and so on. Like that I get two smaller lists, one with big elements and one with small.
To return the final list, the last elemnt of final list will be last element of bigger list. So always the last big
will have big.next as None. And we will also have to join the last smaller to first bigger. To complete the list. 
And then finally we will return the first smallest (in this case 2). So apart from the iteration, it is also thus imp
to keep in memory the refernce of first big (so that last small can join it) and the very first small (so we can return
that). """
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        default = head
        b = s = None
        ret = temp = None
        while head:
            if head.val < x:
                s = head
                if not ret:
                    ret = head #first small which will be returned. First node of final list
            elif head.val >= x:
                b = head
                if not temp:
                    temp = head #first large to which last small will be joined.
            head = head.next
            if s and b:
                break
        else:
            return default

        while head:
            if head.val < x:
                s.next = head
                s = head
            else:
                b.next = head
                b = head
            head = head.next
        b.next = None
        s.next = temp
        return ret
