"""
Question: Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False
"""

# Solution - 1 | time complexity - O(m+m+mlogm + n+n+nlogn) where m = length of sentence_1, n = length of sentence_2
def check_anagram(sentence_1,sentence_2):
  sentence_1=sentence_1.lower()
  sentence_2=sentence_2.lower()
  sentence_1=sentence_1.replace(" ", "")
  sentence_2=sentence_2.replace(" ", "")
  sentence_1 = sorted(sentence_1)
  sentence_2 = sorted(sentence_2)
  if sentence_1 == sentence_2:
    return True
  else:
    return False
if __name__ == "__main__":
  s = "Astronomer"; t = "Moon starer"
  print(check_anagram(s,t))
  
  
# Solution - 2 | time complexity - O(m+n) where m = length of sentence_1, n = length of sentence_1
def check_anagram(sentence_1,sentence_2):
  dic_sen_1={}
  for i in sentence_1:
    i=i.lower()
    if i==" ":
      continue
    if i in dic_sen_1:
      dic_sen_1[i]+=1
    else:
      dic_sen_1[i]=1
  for j in sentence_2:
    j=j.lower()
    if j==" ":
      continue
    if j not in dic_sen_1:
      return False
    else:
      dic_sen_1[j]-=1
      if dic_sen_1[j]==0:
        del dic_sen_1[j]
  if dic_sen_1=={}:
    return True
  else:
    return False
if __name__ == "__main__":
  s = "Astronomer"; t = "Moon starer"
  print(check_anagram(s,t))
  s1 = "anagram"; t1 = "nagaram"
  print(check_anagram(s1,t1))
