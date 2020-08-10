"""
Question: Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.

The function should find all quadruplets in the array that sum up to the largest sum and return a two dimensional array of all these quadruplets in no particular order.

This is the last of its kind, I hope you would have understood the concept of storing complements in the set / dictionary or after sorting the list we can use two pointers to decide whether to decrement / increment the pointers. This problem also works on the similar principle, so don't get trapped into the 4 loop Naive Solution.

Sample Input 1:
array = [7,6,4,-1,1,2]
targetSum = 16

Sample Output 1:
// the quadruplets could be ordered differently
[[7, 6, 4, -1], [7, 6, 1, 2]]

Optimal Space & Time Complexity:
Average: O(n^2) time | O(n^2) space - where n is the length of the input arrayTwo
Worst: O(n^3) time | O(n^2) space - where n is the length of the input array
"""

# Solution - 1
def fourNumberSum(array, targetSum):
    result=[]
    len_array=len(array)
    for i in range(len_array):
      temp1=targetSum-array[i]
      list1=[]
      for j in range(i+1, len_array):
        temp2=temp1-array[j]
        for z in range(j+1, len_array):
          temp3=temp2-array[z]
          if temp3 in list1:
            ans=[array[i], array[j], array[z], temp3]
            ans.sort()
            if ans not in result:
              result.append(ans)
          else:
            list1.append(temp3)
    return result
  
if __name__ == "__main__":
  array = [7,6,4,-1,1,2]
  targetSum = 16
  output = fourNumberSum(array, targetSum)
  print(output)
  

# Solution - 2
def fourNumberSum(array, targetSum):
    array = sorted(array)
    result=[]
    len_array=len(array)
    for i in range(len_array-1):
      for j in range(i+1, len_array-1):
        diff = targetSum-array[i]-array[j]
        start = j+1
        end = len_array-1
        while start<end:
          a=array[start]
          b=array[end]
          if diff==(a+b):
            result.append([array[i], array[j], array[start], array[end]])
            start+=1
          elif diff>(a+b):
            start+=1
          else:
            end-=1
    return result

if __name__ == "__main__":
  array = [7,6,4,-1,1,2]
  targetSum = 16
  output = fourNumberSum(array, targetSum)
  print(output)
  
