"""
Question: Three Number Sum
Write a function that takes in a non empty array of distinct integers and an integer representing a target sum. 
The function should find a list of triplets in the array that sum upto the target sum and return a two-dimensional array of all the these triplets.
The numbers in each triplet should be order in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
If no three numbers sum up to the target sum, the function should return an empty array.
Sample Input 1
array = [12, 2,1, 3, -6, 5, -8, 6]
targetSum = 0
Sample Output 1
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""
    

def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    n = len(array)
    result = []
    for i in range(n - 1):
      for m in range(i+1,n):
        num = targetSum - (array[i] + array[m]) 
        if num in array and num != array[i] and num != array[m]:
          if sorted([array[i], array[m], num]) not in result:
            result.append(sorted([array[i], array[m], num]))
    return result
    
    
if __name__ == '__main__':
  array =  [12, 2, 1, 3, -6, 5, -8, 6]
  targetSum = 0
  print(threeNumberSum(array, targetSum))
