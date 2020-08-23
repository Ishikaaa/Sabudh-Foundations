"""
Question: Strictly Increasing Numbers

Print all n-digit strictly increasing numbers
Given number of digits n in a number, print all n-digit numbers whose digits are strictly increasing from left to right.

Examples:
Sample Input 1: n = 2
Sample Output 1:  
['01', '02', '03', '04', '05', '06', '07', '08', '09', '12', '13', '14', '15', '16', '17', '18', '19', '23', '24', '25', '26', '27', '28', '29', '34', '35', '36', '37', '38', '39', '45', '46', '47', '48', '49', '56', '57', '58', '59', '67', '68', '69', '78', '79', '89']

Sample Input 2: n = 1
Sample Output 2: ['01', '02', '03', '04', '05', '06', '07', '08', '09']
"""

def is_strictly_increasing(number):
    for i in range(len(number)-1):
        if int(number[i])>=int(number[i+1]):
            return False
    return True

def strictly_increasing(input_number):
    res = []
    last_number = "9"*input_number
    if input_number == 1:
        return ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    first_number = "0"
    for i in range(1, input_number):
        first_number = first_number + str(i)
    while int(first_number)<=int(last_number):
        if is_strictly_increasing(first_number):
            a = "0"*(input_number-len(first_number))+first_number
            res.append(a)
        first_number = str(int(first_number)+1)
    return res

if __name__ == "__main__":
    input_number = 1
    print(strictly_increasing(input_number))
