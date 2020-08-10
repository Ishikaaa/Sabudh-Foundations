"""
Question: Move Element to End

You're given an array of integers and an integer. Write a function that moves all instance of that integer in the array to the end of the array and returns the array.

Write a function that should perform this in place (i.e , it should mutate the input array) and doesn't need too maintain the order of the other integer.

Sample Input 1:
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

Sample Output 1:
[1, 3, 4, 2, 2,2,2,2] // the number 1, 3, and 4 could be ordered differently

Time Complexity:
O(n) time | O(1) space,
where n, is the length of the array
"""

# Solution - 1 | time complexity - O(n^2)
def moveElementToEnd(array, toMove):
    i=0
    j=len(array)-1
    while (i<j):
      while array[j]==toMove:
          j-=1
      if array[i]==toMove and i<j:
        array[i], array[j] = array[j], array[i]
        j-=1
      i+=1
    return array
if __name__ == "__main__":
  array = [2, 1, 2, 2, 2, 3, 4, 2]
  toMove = 2
  print(moveElementToEnd(array, toMove))
  
  
# Solution - 2 | time complexity - O(n)
def moveElementToEnd(array, toMove):
    len_array=len(array)
    for i in range(len_array-1, -1, -1):
        if array[i]==toMove:
            array.pop(i)
            array.append(toMove)
    return array    
if __name__ == "__main__":
  array = [2, 1, 2, 2, 2, 3, 4, 2]
  toMove = 2
  print(moveElementToEnd(array, toMove))
