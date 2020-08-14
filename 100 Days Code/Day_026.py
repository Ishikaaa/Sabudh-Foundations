"""
Question: Keys And Rooms

There are N rooms and you start in room 0. Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0). You can walk back and forth between rooms freely.Return true if and only if you can enter every room.

Example 1:
Input: [[1],[2],[3],[]]
Output: True
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.

Example 2:
Input: [[1,3],[3,0,1],[2],[0]]
Output: False
Explanation: We can't enter the room with number 2.

Note:
1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
"""

# Solution - 1
def canVisitAllRooms(rooms):
  visited=[]
  unvisited=[0]
  all_keys=[0]
  while_loop_word=True
  while while_loop_word and unvisited!=[]:
    for i in range(len(unvisited)-1, -1, -1):
      visited.append(unvisited[i])
      if rooms[unvisited[i]]==[]:
        continue
      if set(rooms[unvisited[i]]).issubset(set(all_keys)):
        visited.extend(unvisited[:i])
        while_loop_word=False
        break
      all_keys.extend(rooms[unvisited[i]])
      all_keys=list(dict.fromkeys(all_keys))
    unvisited=[]
    for j in all_keys:
      if j not in visited:
        unvisited.append(j)
  n=len(rooms)
  for z in range(n):
    if z not in visited:
      return False
  return True
  
if __name__ == "__main__":
  rooms = [[1],[2],[3],[]]
  print(canVisitAllRooms(rooms))
  

# Solution - 2
def canVisitAllRooms(rooms):
  key_stack = [0]
  rooms_visited = [0]*len(rooms)
  rooms_visited[0]=1
  while key_stack:
    k = key_stack.pop()
    if rooms_visited[k] == 0:
      rooms_visited[k]=1
    for new_key in rooms[k]:
      if rooms_visited[new_key]==0:
        key_stack.append(new_key)
        #stack.extend(rooms[k])
  for flag in rooms_visited:
    if flag==0:
      return False
  return True

if __name__ == "__main__":
  rooms = [[1],[2],[3],[]]
  print(canVisitAllRooms(rooms))
