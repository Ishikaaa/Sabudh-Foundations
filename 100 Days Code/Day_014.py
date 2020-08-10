"""
Question: Remove Nth Node From End

Given a linked list, remove the n-th node from the end of the list and return its head.

Example: Given linked list: 1->2->3->4->5, and n = 2.
Explanation: After removing the second node from the end, the linked list becomes 1->2->3->5.

Note: Given n will always be valid.
"""

# Solution -1 | time complexity - O(m+n) where m=length of linked list, m=position of nth node
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp=head
        len_head=1
        # get length of linked list
        while temp.next!=None:
            len_head+=1
            temp=temp.next
        # get position from start of the list 
        n = len_head-n+1
        # remove n-th node from start of the list
        temp=head
        count=2
        if n == 1:
            head=head.next
            return head
        while temp.next!=None and count<n:
            temp=temp.next
            count+=1
        a=temp.next
        temp.next=temp.next.next
        a.next=None
        return head


# Solution -2 | time complexity - O(m) where m=length of linked list
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next==None:
            if n==1:
                return head.next
        temp_b=head
        temp_a=head
        for i in range(n):
            temp_b=temp_b.next
        if temp_b==None:
            return head.next
        while temp_b.next!=None:
            temp_b=temp_b.next
            temp_a=temp_a.next
        temp_a.next=temp_a.next.next
        return head
