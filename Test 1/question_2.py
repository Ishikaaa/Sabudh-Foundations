"""
Question: Count Platforms

Given two arrays (both of size n), one containing arrival time of trains and other containing the corresponding trains departure time (in the form of an integer) respectively. Return the minimum number of platform required, such that no train waits. Arrival and departure time of a train can't be same. 

Input Format:
Line 1: Integer n, number of elements in arrival and departure array
Line 2: Elements of Arrival Array (separated by spaces).
Line 3: Elements of Departure Array (separated by spaces).
Output Format:
Minimum Number of Platform Needed

Constraints :
1 <= n <= 100

Sample Input 1: 6
900 940 950 1100 1500 1800
910 1200 1120 1130 1900 2000
Sample Output 1: 3

Sample Input 2: 4
1100 1101 1103 1105
1110 1102 1104 1106
Sample Output 2: 2
"""

def answer(A, B):
  trains=len(A)
  no_of_platforms=[]
  len_platforms=0
  for i in range(trains):
    t=A[i]
    for j in range(len(no_of_platforms)-1, -1, -1):
      if len(no_of_platforms)>len_platforms:
        len_platforms=len(no_of_platforms)
      if(t>no_of_platforms[j][1]):
        no_of_platforms.remove(no_of_platforms[j])
    a=(i, B[i])
    no_of_platforms.append(a)
  return len_platforms

n=int(input())
arrival = list(map(int, input().split()))
depature = list(map(int, input().split()))
print(answer(arrival, depature))
