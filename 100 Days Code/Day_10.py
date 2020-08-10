"""
Question: Ceasar Cipher Encryptor

Given a non-empty string of lowercase letters and a non-negative integer representing a key, Write a function that returns a new string obtained by shifting any letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by one returns the letter "a"

Sample Input 1:
string = "xyz"
key = 2

Sample Output 1:
"zab"

Optimal Space & Time Complexity 1:
O(1) & O(n), where n is the length of the input string. 
"""

def caesarCipherEncryptor(string, key):    
  while key>25:
    key=key-25-1
  result=''
  for i in string:
    ascii_i=ord(i)
    ascii_i+=key
    if ascii_i>122:
      diff=ascii_i-122
      ascii_i=97+diff-1
    result=result+chr(ascii_i)  
  return result
 
if __name__=="__main__":
  string = "abc"
  key = 57
  print(caesarCipherEncryptor(string, key))

  string = "xyz"
  key = 2
  print(caesarCipherEncryptor(string, key))
