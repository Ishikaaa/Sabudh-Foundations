"""
Question: Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non -decreasing.

Sample Input 1:
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output 1:
True

Time Complexity: 
O(n) time | O(1) space, where n, is the length of the array
"""

def monoArray(array):
  if len(array)<=2:
    return True
  if array[0]>array[1]:
    for i in range(1, len(array)-1):
      if array[i]<array[i+1]:
        return False
    return True
  else:
    for i in range(1, len(array)-1):
      if array[i]>array[i+1]:
        return False
    return True
if __name__ == "__main__":
  array = [-1, -5, -10, -1100, -1100 -1101, -1102, -9001]
  print(monoArray(array))
  array = [1, 100, 10000]
  print(monoArray(array))
