"""
Question: Rotated Left By 2

Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

Sample Input 1 -> Output
rotate2('Hello') → 'lloHe'
rotate2('java') → 'vaja'
"""

# Solution - 1
def rotate2(a):
  b=a[2:]+a[:2]
  print(b)
if __name__=="__main__":
  a=input()
  rotate2(a)
  
# Solution - 2
def rotate2(a):
  for i in range(2):
    a=a[1:]+a[:1]
  print(a)
if __name__=="__main__":
  a=input()
  rotate2(a)
