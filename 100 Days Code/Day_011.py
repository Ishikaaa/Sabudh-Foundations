"""
Question: Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false.

Sample input 1:
items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
items.search_item('SQL')

Sample output 1:
False
"""

class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Create an empty list
        self.tail = None
        self.head = None
        self.count = 0
    
    def append_item(self, data):
        if self.count==0:
            self.head=Node(data)
            self.tail=self.head
            self.count+=1
            return 
        self.count+=1
        self.tail.next=Node(data)
        self.tail=self.tail.next
        return 
      
    def print_linked_list(self):
        # print the list
        temp=self.head
        for i in range(self.count):
            print(temp.data)
            temp=temp.next
          
    def search_item(self, val):
        # Search the list
        temp=self.head
        for i in range(self.count):
            if temp.data==val:
                return True
            temp=temp.next
        return False
          
if __name__ == "__main__":
    items = singly_linked_list()
    items.append_item('SQL')
    items.append_item('Python')
    items.append_item('C#')
    items.append_item('C++')
    items.append_item('Java')
    
    items.print_linked_list()
    
    print(items.search_item('SQL1'))
