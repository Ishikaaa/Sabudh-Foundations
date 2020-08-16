"""
Question: Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,4,7,5,3,6,8,9]
Explanation:.....

Note:
The total number of elements of the given matrix will not exceed 10,000.
"""

def return_diag(input_matrix):
    if input_matrix == []:
        return []
    row = len(input_matrix)
    column = len(input_matrix[0])
    dict_input_matrix={}
    for i in range(row):
        for j in range(column):
            sum=i+j
            if sum in dict_input_matrix:
                dict_input_matrix[sum].append([i, j])
            else:
                dict_input_matrix[sum] = [[i, j]]
  
    result = []
    for key, value in dict_input_matrix.items():
        if key%2!=0:
            for i in value:
                result.append(input_matrix[i[0]][i[1]])
        else:
            temp=[]
            for i in value:
                temp.append(input_matrix[i[0]][i[1]])
            result.extend(temp[::-1])
    return result

if __name__ == "__main__":
    input_matrix = [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
      ]
    print(return_diag(input_matrix))

    input_matrix = [
     [ 1, 2, 3, 4, 5 ],
     [ 6, 7, 8, 9, 10],
     [ 11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20]
       ]
    print(return_diag(input_matrix))
