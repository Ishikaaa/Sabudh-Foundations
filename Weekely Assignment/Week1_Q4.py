"""
Question: Arrow Pattern

Print the following pattern for the given number of rows. Assume N is always odd. Note : There is space after every star. Pattern for N = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*

Input format: Integer N (Total no. of rows)
Output format: Pattern in N lines

Sample Input 1: 11
Sample Output 1:
*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*
"""

n=int(input())
n_half=int(n/2)
space_index=1
print("*")
for i in range(2, n_half+2):
  print(" "*space_index+"* "*(i-1), end="")
  print("*")
  space_index+=2
space_index-=2
for j in range(n_half, 1, -1):
  space_index-=2
  print(" "*space_index+"* "*(j-1), end="")
  print("*")
print("*")
