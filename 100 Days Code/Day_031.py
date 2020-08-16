"""
Question: Introduction To Recussion

Write a Python program of recursion list sum.

Example 1:
Input: grid = [1, 2, [3,4],[5,6]]
Output: 21
"""

def recursive_sum(input_matrix, sum=0):
    sum=0
    for i in input_matrix:
        if isinstance(i, int):
            sum+=i
        else:
            sum+=recursive_sum(i, sum)
        print(i, sum)
    return sum
    
if __name__ == "__main__":
  input_matrix = [1, 2, [3,4],[5,6]]
  print(recursive_sum(input_matrix))
