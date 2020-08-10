"""
Question: Hunt a new Apartment

You're looking to move into a new apartment, and you're given a list of blocks where each block contains an apartment that you could move into. In order to pick your apartment, you want to optimize its location. 
You also have a list of requirements: a list of buildings that are important to you. For instance, you might value having a school and a gym near your apartment.
The list of blocks that you have contains information at every block about all of the buildings that are present and absent at the block in question.
For instance, for every block, you might know whether a school, a pool, an office, and a gym are present.
In order to optimize your life, you want to minimize the farthest distance you'd have to walk from your apartment to reach any of your required buildings.
Write a function that takes in a list of blocks and a list of your required buildings and that returns the location (the index) of the block that's most optimal for you.

Sample Imput 1:
blocks = [
 {"gym": false, "school": true, "store": false},
 {"gym": true, "school": false, "store": false},
 {"gym": true, "school": true, "store": false},
 {"gym": false, "school": true, "store": false},
 {"gym": false, "school": true, "store": true}
]
reqs = ["gym", "school", "store"]

sample output 1:
3 

Explanation:
At index 3, the farthest you'd have to walk to reach a gym, school, or a store is 1 block; at any other index, you'd have to walk farther
"""

def apartmentHunting(blocks, reqs):
  len_blocks=len(blocks)
  farthest_distance={}
  len_reqs=len(reqs)

  for j in range(len_reqs):
    current_reqs_list = [float('inf')]*len_blocks
    current_reqs=reqs[j]
    if blocks[0][current_reqs]==True:
      current_reqs_list[0]=0
    for i in range(1, len_blocks):
      i_element=blocks[i]
      if i_element[current_reqs]==True:
        current_reqs_list[i]=0
      else:
        current_reqs_list[i]=current_reqs_list[i-1]+1
    for j in range(len_blocks-2, -1, -1):
      j_element=blocks[j]
      if j_element[current_reqs]==True:
        current_reqs_list[j]=0
      else:
        min_value=min(current_reqs_list[j+1]+1, current_reqs_list[j])
        current_reqs_list[j]=min_value
    farthest_distance[current_reqs]=current_reqs_list
  result_list=[]
  
  for i in range(len_blocks):
    a=[]
    for j in range(len_reqs):
      req=reqs[j]
      a.append(farthest_distance[req][i])
    max_a=max(a)
    result_list.append(max_a)
  max_result_list=min(result_list)
  return result_list.index(max_result_list)

if __name__=="__main__":
  false=False
  true=True
  blocks = [
   {"gym": false, "school": true, "store": false},
   {"gym": true, "school": false, "store": false},
   {"gym": true, "school": true, "store": false},
   {"gym": false, "school": true, "store": false},
   {"gym": false, "school": true, "store": true}
  ]
  reqs = ["gym", "school", "store"]
  print(apartmentHunting(blocks, reqs))
