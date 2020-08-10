"""
Question: Three Number Sum

Write a function that takes in a non empty array of distinct integers and an integer representing a target sum. 

The function should find a list of triplets in the array that sum upto the target sum and return a two-dimensional array of all the these triplets.

The numbers in each triplet should be order in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.

Sample Input 1:
array = [12, 2,1, 3, -6, 5, -8, 6]
targetSum = 0

Sample Output 1:
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""

def threeNumberSum(array, targetSum):
    ans=[]
    len_array=len(array)
    
    # sorting array
    for i in range(len_array):
      for j in range(i+1, len_array):
        if array[i]>array[j]:
          array[i], array[j] = array[j], array[i]
    
    # finding three sum array 
    for i in range(len_array):
      for j in range(i+1, len_array):
        remain=targetSum-array[i]-array[j]
        if remain in array[i+1:] and array.index(remain)!=i and array.index(remain)!=j:
          a1=min(array[i], array[j], remain)
          a3=max(array[i], array[j], remain)
          a2=(array[i]+array[j]+remain)-(a1+a3)
          if [a1, a2, a3] not in ans:
            ans.append([a1, a2, a3])
    return ans
    
if __name__ == '__main__':
  array =  [12, 2, 1, 3, -6, 5, -8, 6]
  targetSum = 0
  print(threeNumberSum(array, targetSum))
  
