"""
Question: Number Pattern

Print the following pattern for n number of rows. 

For eg: N = 5
1        1
12      21
123    321
1234  4321
1234554321

Sample Input 1: 4
Sample Output 1:
1      1
12    21
123  321
12344321
"""

n=int(input())
for i in range(1, n+1):
  for j in range(1, i+1):
    print(str(j), end="")
  print(" "*(2*(n-i)), end="")
  for j in range(i, 0, -1):
    print(j, end="")
  print()
