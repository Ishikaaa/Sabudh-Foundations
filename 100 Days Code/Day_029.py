"""
Question: Number Of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

def count_island(input_matrix):
    n=len(input_matrix)
    m=len(input_matrix[0])
    island=1
    for i in range(n):
        for j in range(m):   
            if input_matrix[i][j]=="1":
                i1=i-1
                j1=j-1
                change=True
                if i1>=0:
                    if input_matrix[i1][j]!="0":
                        input_matrix[i][j] = input_matrix[i1][j]
                        change = False
                if j1>=0:
                    if input_matrix[i][j1]!="0":
                        input_matrix[i][j] = input_matrix[i][j1]
                        change = False
                if change==True:
                    input_matrix[i][j] = str(island)
                    island += 1
    for i in input_matrix:
      print(i)
    return island-1
if __name__ == "__main__":
  input_matrix = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
  ]
  print(count_island(input_matrix))

  input_matrix = [
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
  print(count_island(input_matrix))

  
