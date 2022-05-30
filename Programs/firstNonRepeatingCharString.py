# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Input: s = "leetcode"
# Output: 0
# Input: s = "loveleetcode"
# Output: 2
s ="leetcode"
setS = set(s)
# print(list(setS))
# print(list(s)- list(setS))
# for i in setS:
#     if i in s:
dict ={}
for i in s:
    if s.count(i) ==1:
        print(f"True. the character is {s.index(i)}")
        break
    else: pass
print(-1)
#     if i not in dict:
#         dict[i] = s.count(i)
# for key,value in dict.items():
#     if value == 1:
#         print(f'The character is "{s.index(key)}"')
#     else:
#         pass
# print(-1) 
# print(dict)




