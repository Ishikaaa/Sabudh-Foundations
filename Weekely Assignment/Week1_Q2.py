"""
Question: Number Pattern

Print the following pattern Pattern for N = 4 1 23 345 4567 

Input Format: N (Total no. of rows)
Output Format: Pattern in N lines

Sample Input 1: 4
Sample Output 1:
   1
  23
 345
4567
"""

n=int(input())
for i in range(1, n+1):
  print(" "*(n-i), end="")
  element=i
  for j in range(i):
    print(element, end="")
    element+=1
  print()
