"""
Question: All Possible Palindromic Partitions

Given a string, find all possible palindromic partitions of given string.

Sample Input 1: nitin
Sample Output 1: 
n i t i n
n iti n
nitin

Sample Input 2: geeks
Sample Output 2:
g e e k s
g ee k s

The idea is to go through every substring starting from first character, check if it is palindrome. If yes, then add the substring to solution and recur for remaining part.
"""


def check_pelidrome(input_string):
    return input_string==input_string[::-1]

def giving_space(input_string):
    a = ""
    for i in input_string:
        a+=i+" "
    return a[:-1]

def recursive_palindrome(input_string):
    result=[giving_space(input_string)]
    len_input_string = len(input_string)
    for i in range(len_input_string):
        for j in range(i+2, len_input_string+1):
            if check_pelidrome(input_string[i:j]):
                a = giving_space(input_string[:i]) +" "+ input_string[i:j] +" "+ giving_space(input_string[j:])
                a = a.strip()
                result.append(a)
    if check_pelidrome(input_string):
        if input_string not in result:
            result.append(input_string)
    return result

if __name__ == "__main__":
    input_string = "nitin"
    print(recursive_palindrome(input_string))

    input_string = "geeks"
    print(recursive_palindrome(input_string))

    input_string = "banana"
    print(recursive_palindrome(input_string))
