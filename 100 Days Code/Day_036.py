"""
Question: Generate All Passwords From The Given Character Set

Given a set of characters generate all possible passwords from them. This means we should generate all possible permutations of words using the given characters, with repetitions and also upto a given length.

Examples:
Input: hack_it({a, b},2)
Output:
['a', 'b', 'aa', 'ab', 'ba', 'bb']
"""

def possible_passwords(chars, i,ans, temp, length):
    if i==0:
        temp.append(ans)
        return 
    for j in range(0, length): 
        a = ans+chars[j]
        possible_passwords(chars, i-1, a, temp, length)    
    return temp

def hack_it(chars,length):
    res=[]
    if length<=0:
        return []
    for i in range(1, length+1):
        temp=[]
        res.extend(possible_passwords(chars, i, "", temp, length))
    return res

if __name__ == "__main__":
    chars = ['a',"b"] 
    print(hack_it(chars,len(chars)))
