"""
Question: Find Target

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
* Integers in each row are sorted from left to right.
* The first integer of each row is greater than the last integer of the previous row.


Sample Input 1:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Sample Output 1: True

Sample Input 2:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Sample Output 2: False
"""

# Using Binary Search
def find_target(input_matrix,target):
  m=len(input_matrix)       # number of rows
  n=len(input_matrix[0])    # number of columns
  a=0                       # Starting pointer 
  b=m*n-1                   # Ending pointer
  while a<=b:
    mid = int((a+b)/2)      
    row=int(mid/n)
    column=mid%n
    if input_matrix[row][column]==target:
      return True
    elif input_matrix[row][column]<target:
      a=mid+1
    else:
      b=mid-1
  return False
  
if __name__ == "__main__":
  input_matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
  ]
  target = 3
  print(find_target(input_matrix,target))
