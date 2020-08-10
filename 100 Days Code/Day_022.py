"""
Question: Get Dictionary Value

Given a dictionary with nested dictionaries as values, extract all the values with of particular key.

Sample Input -> Output

Input : test_dict = {‘sup’ : {“a” : 7, “b” : 9, “c” : 12}, ‘is’ : {“a” : 15, “b” : 19, “c” : 20}, ‘best’ :{“a” : 5, “b” : 10, “c” : 2}}, temp = “b”
Output : [9, 10, 19]
Explanation : All values of “b” key are extracted.

Input : test_dict = {‘sup’ : {“a” : 7, “b” : 9, “c” : 12}, ‘is’ : {“a” : 15, “b” : 19, “c” : 20}, ‘best’ :{“a” : 5, “b” : 10, “c” : 2}}, temp = “a”
Output : [7, 15, 5]
Explanation : All values of “a” key are extracted.
"""

# Solution - 1 | time complexity - O(n*m) where n = length of outer dictionary, m = length of inner dictionary
def get_key(input_dict,key):
  res=[]
  for j in input_dict.values():
    for i, z in j.items():
      if i==key:
        res.append(z)
  return res
if __name__ == "__main__":
  input_dict = {
    'sup' : {"a" : 7, "b" : 9, "c" : 12}, 
		'is' : {"a" : 15, "b" : 19, "c" : 20}, 
		'best' :{"a" : 5, "b" : 10, "c" : 2}
  }
  key = "b"
  print(get_key(input_dict,key))
  
  
# Solution - 2 | time complexity - O(n) where n = length of outer dictionary
def get_key(input_dict,key):
  res=[]
  for i in input_dict.values():
    if key in i.keys():
      res.append(i[key])
  return res
if __name__ == "__main__":
  input_dict = {
    'sup' : {"a" : 7, "b" : 9, "c" : 12}, 
		'is' : {"a" : 15, "b" : 19, "c" : 20}, 
		'best' :{"a" : 5, "b" : 10, "c" : 2}
  }
  key = "b"
  print(get_key(input_dict,key))
