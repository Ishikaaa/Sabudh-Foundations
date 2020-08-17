"""
Question: Number Of Paths That Sum To Given Value

You are given a binary tree in which each node contains an integer value.Find the number of paths that sum to a given value.The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,None,11,3,-2,None,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

def spilt_array(input_matrix, sum_first_element, array, a):
    if sum_first_element == len(input_matrix):
        array.append(input_matrix)
        return
    left=input_matrix[:sum_first_element]
    right=input_matrix[:sum_first_element]
    a=1
    ele_left=a
    ele_right=a
    for i in input_matrix[sum_first_element:]:
        if i==None:
            i=0
        if ele_left==0 and ele_right==0:
            a*=2
            ele_left=a
            ele_right=a
        if ele_left==0 and ele_right>0:
            right.append(i)
            ele_right-=1
        if ele_left>0:
            left.append(i)
            ele_left-=1
    spilt_array(left, sum_first_element+1, array, a)
    spilt_array(right, sum_first_element+1, array, a)
    return array

def sum_tree(input_matrix,sum_val):
    array=[]
    a=1
    sum_first_element = 1
    result = []
    all_paths = spilt_array(input_matrix, sum_first_element, array, a)
    for i in all_paths:
        if sum(i[1:-1]) == sum_val:
            if i[1:-1] not in result:
                result.append(i[1:-1])
        if sum(i[:-1]) == sum_val:
            if i[:-1] not in result:
                result.append(i[:-1])
        if sum(i[1:]) == sum_val:
            if i[1:] not in result:
                result.append(i[1:])
    return len(result)

if __name__ == "__main__":
    input_matrix = [10,5,-3,3,2,None,11,3,-2,None,1]
    sum_val = 8
    print(sum_tree(input_matrix,sum_val))
