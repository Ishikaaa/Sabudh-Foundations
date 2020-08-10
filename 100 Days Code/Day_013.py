"""
Question: Check Palidrome

Function to check if a singly linked list is a palindrome
Given a singly linked list of characters, write a function that returns True if the given list is a palindrome, else False.

Sample input 1:
("r" -> "a" -> "d" -> "a" -> "r" )

Sample output 1:
True
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def checkPalindrome(self, l1: ListNode):
        if l1==None:
            return True
        array=[]
        while l1.next!=None:
            array.append(l1.val)
            l1=l1.next
        array.append(l1.val)
        a=0
        b=len(array)-1
        while a<=b:
            if array[a]!=array[b]:
                return False
            a+=1
            b-=1
        return True
