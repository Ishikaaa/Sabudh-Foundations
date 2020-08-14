"""
Question: Swap Alternate

You have been given an array/list of size N. You need to swap every pair of alternate elements in the array/list. You have to change the input array itself and print the result

Input Format:
First line of each test case or query contains an integer 'N' representing the size of the array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.
Output Format :
For each test case, print the elements of the resulting array in a single row separated by a single space.
Output for every test case will be printed in a separate line.

Constraints:
1 <= t <= 10^2
0 <= N <= 10^5
Time Limit: 1sec

Sample Input 1:
1
6
9 3 6 12 4 32
Sample Output 1:
3 9 12 6 32 4

Sample Input 2:
2
9
9 3 6 12 4 32 5 11 19
4
1 2 3 4
Sample Output 2:
3 9 12 6 32 4 11 5 19 
2 1 4 3 
"""

def reverse_list(A):
  iterate_list=int(len(A)/2)
  for i in range(iterate_list):
    a=(2*i-1)+1
    b=a+1
    A[a], A[b]=A[b], A[a]
  return A

num_test_cases=int(input())
B=[]
for i in range(num_test_cases):
  num_inputs=int(input())
  A = list(map(int, input().split()))
  B.append(reverse_list(A))
for list_ in B:
  for j in range(len(list_)-1):
    print(list_[j], end=" ")
  print(list_[-1])
  
