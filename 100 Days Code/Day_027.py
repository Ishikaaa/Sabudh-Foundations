"""
Question: Print Words Vertically

Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

Example 1:
Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"

Example 2:
Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
"""

def return_vertically(input_string):
    li=input_string.split()
    n=max(len(x) for x in li)
    m=len(li)
    res=[[" " for j in range(m)] for i in range(n)]
    for j in range(m):
        x=li[j]
        for i in range(len(x)):
            res[i][j]=x[i]
    ans=[]
    for x in res:
        y="".join(map(str,x))
        y=y.rstrip()
        ans.append(y)
    return ans
  
if __name__ == "__main__":
  input_string = "HOW ARE YOU"
  print(return_vertically(input_string))
  input_string = "TO BE OR NOT TO BE"
  print(return_vertically(input_string))
