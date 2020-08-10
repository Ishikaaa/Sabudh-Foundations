"""
Question: Maximum Of Each Column

Write a  program to find maximum of each column of  2d array 

Sample Input -> Output
max_col([[1, 5, 13], [11], [9, 18]]) → [11, 18, 13] 
max_col([[1, 8, 1], [1,21], [9]]) → [9, 21, 1]
"""

# Solution - 1
import itertools 
def max_col(test_list):
    test_list.sort(reverse=True)
    res=[]
    m=0
    len_test_list=len(test_list)
    while m<len_test_list:
        a=set([])
        for i in range(m, len_test_list):
            a.add(test_list[i][m])
        res.append(max(a))
        m+=1
    return res
if __name__ == "__main__":
  input_list = [[1, 8, 1], [1,21], [9]]
  print(max_col(input_list))
  

# Solution - 2
import itertools 
def max_col(test_list):
    len_test_list=len(test_list)
    res=[-1]*len_test_list
    for i in test_list:
        for j in range(len(i)):
            if res[j]<i[j]:
                res[j]=i[j]
    return res
if __name__ == "__main__":
  input_list = [[1, 8, 1], [1,21], [9]]
  print(max_col(input_list))
  
  
# Solution - 3
import itertools 
def max_col(test_list):
    res=[]
    len_test_list=len(test_list)
    for i in test_list:
        if len(res)<len(i):
            res=res+[-1]*(len(i)-len(res))
        for j in range(len(i)):
            if res[j]<i[j]:
                res[j]=i[j]
    return res
if __name__ == "__main__":
  input_list = [[1, 8, 1], [1,21], [9]]
  print(max_col(input_list)) 
