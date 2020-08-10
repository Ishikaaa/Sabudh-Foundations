"""
Question: Add Numbers In Linked List

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Sample input 1:
(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)

Sample output 1:
7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      a1=0
      a2=0
      while l1.next!=None:
          a1=a1*10+l1.val
          l1=l1.next
      a1=a1*10+l1.val
      
      while l2.next!=None:            
          a2=a2*10+l2.val
          l2=l2.next
      a2=a2*10+l2.val
      
      addition=a1+a2
      
      str_addition=str(addition)
      sum_l1_l2=ListNode(int(str_addition[0]))
      temp=sum_l1_l2
      for i in str_addition[1:]:
          temp.next=ListNode(int(i))
          temp=temp.next
      return sum_l1_l2
