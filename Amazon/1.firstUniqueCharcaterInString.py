# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# s = "leetcode" # 0
s="loveleetcode"

map ={}
for i in s:
    if i not in map:
        map[i] =1
    else:
        map[i]+=1
print(map)
for x in map.items():
    if x[1]==1:
        print(x[0])
        print(s.index(x[0]))
        break