"""
Question: Symmetric Difference

Given 2 sets of integers,  M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  M or N  but do not exist in both.

Input Format:
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format:
Output the symmetric difference integers in ascending order, one per line.

Sample Input 1:
4
2 4 5 9
4
2 4 11 12

Sample Output 1:
5
9
11
12
"""

def symmetric_difference(len_A, len_B, A, B):
  D=A.union(B)
  result=[]
  for i in D:
    if i in A and i in B:
      continue
    result.append(i)
  result.sort()
  for i in result:
    print(i)

if __name__=="__main__":
  a=int(input())
  A = set(map(int, input().split()))
  b=int(input())
  B = set(map(int, input().split()))
  symmetric_difference(a, b, A, B)
