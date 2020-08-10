"""
Question: Number Pattern

Print the following pattern Pattern for N = 4
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 

Input Format: N (Total no. of rows)
Output Format: Pattern in N lines

Sample Input 1: 5
Sample Output 1:
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5
"""

n=int(input())
iteration = 2*n-1
line=(str(n)+" ")*(iteration-1)
line=line+str(n)
list_lines=[line]
for i in range(1, n):
  line=''
  element=n
  line=str(element)+" "
  for j in range(0, i):
    element-=1
    line=line+str(element)+" "
  line=line+(str(element)+" ")*(iteration-2*i-1)
  for j in range(0, i-1):
    element+=1
    line=line+str(element)+" "
  line=line+str(n)
  list_lines.append(line)
for i in list_lines:
  print(i)
for i in range(len(list_lines)-2, -1, -1):
  print(list_lines[i])  
