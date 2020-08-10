"""
Question: Convert Numerical Into Roman Number

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty-seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
* I can be placed before V (5) and X (10) to make 4 and 9. 
* X can be placed before L (50) and C (100) to make 40 and 90. 
* C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: 3
Output: "III"

Example 2:
Input: 4
Output: "IV"

Example 3:
Input: 9
Output: "IX"

Example 4:
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# Solution - 1
def num_conversion(input_number):
  Roman = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
  result=""
  str_number=str(input_number)
  len_number=len(str_number)-1
  for i in str_number:  
    current_number=int(i)*(10**len_number)
    if current_number in Roman:
      result=result+Roman[current_number]
    elif i=="4" or i=="9":
      a=(int(i)+1)*(10**len_number)
      b=1*(10**len_number)
      result=result+Roman[b]+Roman[a]
    elif i=="2" or i=="6":
      a=(int(i)-1)*(10**len_number)
      b=1*(10**len_number)
      result=result+Roman[a]+Roman[b]
    elif i=="3" or i=="7":
      a=(int(i)-2)*(10**len_number)
      b=1*(10**len_number)
      result=result+Roman[a]+Roman[b]*2
    elif i=="8":
      print(len_number)
      a=(int(i)-3)*(10**len_number)
      b=1*(10**len_number)
      result=result+Roman[a]+Roman[b]*3
    len_number-=1
  return result
if __name__ == "__main__":
  input_number =1994
  print(num_conversion(input_number))
  

# Solution - 2
def num_conversion(input_number):
  Roman = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
  result=""
  str_number=str(input_number)
  len_number=len(str_number)-1
  for i in str_number:  
    current_number=int(i)*(10**len_number)
    if current_number in Roman:
      result=result+Roman[current_number]
    elif i=="4" or i=="9":
      a=(int(i)+1)*(10**len_number)
      result=result+Roman[(1*(10**len_number))]+Roman[a]
    elif i=="2" or i=="3":
      result=result+Roman[(1*(10**len_number))]*int(i)
    elif i=="6" or i=="7" or i=="8":
      result=result+Roman[(5*(10**len_number))]+Roman[(1*(10**len_number))]*(int(i)-5)
    len_number-=1
  return result
if __name__ == "__main__":
  input_number =58
  print(num_conversion(input_number))
