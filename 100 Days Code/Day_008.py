"""
Question: Longest Peak

Given an array arr[] with N elements, the task is to find out the longest sub-array which has the shape of a mountain.

The Longest Peak consists of elements that are initially in ascending order until a peak element is reached and beyond the peak element all other elements of the sub-array are in decreasing order.

Sample Input 1: arr = [2, 2, 2] 
Sample Output 1: 0 
Explanation: No sub-array exists that shows the behaviour of a mountain sub-array.

Sample Input 2: arr = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5] 
Sample Output 2: 11 
Explanation: There are two sub-arrays that can be considered as mountain sub-arrays. The first one is from index 0 – 2 (3 elements) and next one is from index 2 – 12 (11 elements).  As 11 > 2, our answer is 11.
"""

def LongestPeak(a): 
  count=0
  max=0
  inc=-1
  for i in range(len(a)-1):
    if a[i]==a[i+1] or (a[i]<a[i+1] and inc==2):
      if count>max:
        max=count+1
      count=0
      inc=0
    if a[i]<a[i+1]:
      count+=1
      inc=1
    if a[i]>a[i+1] and inc!=-1:
      count+=1
      inc=2
  if count>max:
    max=count+1
  return max

if __name__ == "__main__":
  d = [ 1, 3, 1, 4, 5, 6,  
        7, 8, 9, 8, 7, 6, 5 ]
  print(LongestPeak(d)) 
  
  d1 = [2, 2, 2]
  print(LongestPeak(d1)) 
