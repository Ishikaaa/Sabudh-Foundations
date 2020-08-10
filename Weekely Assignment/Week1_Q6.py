"""
Question: Print The Pattern

Print the following pattern for the given number of rows.
Pattern for N = 5
1 2 3 4 5
11 12 13 14 15
21 22 23 24 25
16 17 18 19 20
6 7 8 9 10

Input format : N (Total no. of rows)
Output format: Pattern in N lines

Sample Input 1: 4
Sample Output 1:
1 2 3 4
9 10 11 12
13 14 15 16
5 6 7 8
"""

n=int(input())
iterate_1=n//2
iterate_2=iterate_1*2-1
if n%2!=0:
  iterate_1+=1
  
for i in range(iterate_1):
  element=2*n*i+1
  for j in range(n-1):
    print(element, end=" ")
    element+=1
  print(element)

for k in range(iterate_2, 0, -2):
  element=n*k+1
  for m in range(n-1):
    print(element, end=" ")
    element+=1
  print(element)
