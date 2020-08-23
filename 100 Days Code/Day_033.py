"""
Question: Power Set In Lexicographic Order

This problem is about generating Power set in lexicographical order.

Examples:
Sample Input 1: abc
Sample Output 1: ["a","ab","abc","ac","b","bc","c"]

Sample Input 2: "banana"
Sample Output 2: ['a', 'aa', 'aaa', 'aaab', 'aaabn', 'aaabnn', 'aaan', 'aaann', 'aab', 'aabn', 'aabnn', 'aan', 'aann', 'ab', 'abn', 'abnn', 'an', 'ann', 'b', 'bn', 'bnn', 'n', 'nn']
"""

def lexi_order(input_string, len_input_string, index, res, result):
    if len_input_string<index:
        return 
    if len(res)>0:
        result.add(res)
    for i in range(index+1, len_input_string):
        res+=input_string[i]
        lexi_order(input_string, len_input_string, i, res, result)
        res = res[:len(res)-1]
    return result

def power_set(input_string):
    input_string = ''.join(sorted(input_string)) 
    result=set([])
    len_input_string = len(input_string)
    result = list(lexi_order(input_string, len_input_string, -1, "", result))
    result.sort()
    return result
    
if __name__ == "__main__":
    input_string = "abc"
    print(power_set(input_string))

    input_string = "banana"
    print(power_set(input_string))
