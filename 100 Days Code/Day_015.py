"""
Question: Merge two sorted linked lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given the following linked lists :
5 -> 8 -> 20 
4 -> 11 -> 15
The merged list should be :
4 -> 5 -> 8 -> 11 -> 15 -> 20
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoLinkedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(0)
        temp=head
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                temp.next=ListNode(l1.val)
                l1=l1.next
            else:
                temp.next=ListNode(l2.val)
                l2=l2.next
            temp=temp.next

        if l1!=None:
            temp.next=l1
        else:
            temp.next=l2
            
        return head.next
