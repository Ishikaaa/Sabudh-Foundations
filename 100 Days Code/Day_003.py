"""
Question: Smallest Difference

Write a function that takes in two non-empty arrays of integers, find the pair of numbers (one from each array) whose absolute difference is closet to zero, and returns an array containing these two numbers, with the numbsers, with the number from the first array in the first position.

You can assume that there will only be one pair of numbers with the smallest difference.

Sample Input 1:
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output 1:
[28, 26]

Optimal Solution:
O(nlog(n)) + O(mlog(m) + O(m+n))
where,
n is the size of arrayOne
m is the size of arrayTwo
"""

def smallestDifference(arrayOne, arrayTwo):
  min_diff=abs(arrayOne[0]-arrayTwo[0])
  for i in arrayOne:
    for j in arrayTwo:
      diff = abs(i-j)
      if diff<min_diff:
        min_diff = diff
        a=i
        b=j
  return [a, b]

if __name__ == "__main__":
  arrayOne = [-1, 5, 10, 20, 28, 3]
  arrayTwo = [26, 134, 135, 15, 17]
  print(smallestDifference(arrayOne, arrayTwo))
