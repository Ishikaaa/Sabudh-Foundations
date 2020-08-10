"""
Question: Triangle Of Numbers

Print the following pattern for the given number of rows. Pattern for N = 4 The dots represent spaces.

Input format: Integer N (Total no. of rows)

Output format: Pattern in N lines

Constraints: 0 <= N <= 50

Sample Input 1: 5
Sample Output 1:
        1
      232
    34543
  4567654
567898765

Sample Input 2: 4
Sample Output 2:
      1
    232
  34543
4567654
"""

n=int(input())
for i in range(1, n+1):
  print(" "*(2*(n-i)), end="")
  for j in range(i, i+i):
    print(j, end="")
  for z in range(i+i-2, i-1, -1):
    print(z, end="")
  print()
