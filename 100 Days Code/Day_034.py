"""
Question: Print Valid IP Address

Given a string s containing only digits. Return all possible valid IP addresses that can be obtained from s. You can return them in any order.
A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single points and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

Sample Input 1: s = "1111"
Sample Output 1: ["1.1.1.1"]

Sample Input 2: s = "101023"
Sample Output 2: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
"""

def valid_ip_address(input_string):
    list_input_string = input_string.split(".")
    for i in list_input_string:
        if len(i)>3:
            return False
        if int(i)<0 or int(i)>255:
            return False
        if len(i)>1 and int(i)==0:
            return False
        if len(i)>1 and int(i)!=0 and i[0]=='0':
            return False
    return True

def valid_ip(input_string):
    len_input_string = len(input_string)
    if len(input_string)>12:
        return []
    result = []
    copy_input_string = input_string
    for i in range(1, len_input_string-2):
        for j in range(i+1, len_input_string-1):
            for k in range(j+1, len_input_string):
                copy_input_string = copy_input_string[:k] +"."+ copy_input_string[k:]
                copy_input_string = copy_input_string[:j] +"."+ copy_input_string[j:]
                copy_input_string = copy_input_string[:i] +"."+ copy_input_string[i:]
                if valid_ip_address(copy_input_string):
                    result.append(copy_input_string)
                copy_input_string = input_string
    return result

if __name__ == "__main__":
    input_string = "0000"
    print(valid_ip(input_string))
    
    input_string = "101023"
    print(valid_ip(input_string))
