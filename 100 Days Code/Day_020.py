"""
Question: Remove Leading Zeros Following "."

Write a  program to remove leading zeros following "." from an IP address.

Sample Input -> Output
remZero("216.08.094.196") → "216.8.94.196" 
remZero("016.08.0904.96") → "016.8.904.96"
"""
 
# Solution - 1 | Without Using Regular Expressions
def remZero(ip_addr):
  result = ""
  result = ip_addr.replace('.0', '.')
  return result
if __name__ == "__main__":
  ip = "016.08.0904.96"
  print(remZero(ip))
  
# Solution - 2 | With Regular Expressions
import re
def remZero(ip_addr):
  result = ""
  result = re.sub(r'([.])0+', r'.', ip_addr)
  return result
if __name__ == "__main__":
  ip = "016.08.0904.96"
  print(remZero(ip))
