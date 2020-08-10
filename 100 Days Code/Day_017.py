"""
Question: Reverse K Nodes

Given a singly linked list and an integer K, reverses the nodes of the list K at a time and returns modified linked list.

Example :
Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

NOTE: The length of the list is divisible by K
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapLinkedLists(self, l1: ListNode,key: int) -> ListNode:
        temp=l1
        array=[]
        count=0
        while temp!=None:
            if count==0:
                ar=[]
            ar.append(temp.val)
            count+=1
            if count==key:
                array.append(ar)
                count=0
            if temp.next!=None:
                temp=temp.next
            else:
                break
        if count!=0:
            array.append(ar)
            
        result=ListNode(0)
        new_linked_list=result
        for i in array:
            if len(i)==key:
                for j in range(len(i)-1, -1, -1):
                    new_linked_list.next=ListNode(i[j])
                    new_linked_list=new_linked_list.next
            else:
                for j in i:                    
                    new_linked_list.next=ListNode(j)
                    new_linked_list=new_linked_list.next
        return result.next
