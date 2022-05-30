# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# s = "anagram"
# s ='rat'
s= 'a'
# t = "nagaram"
# t= 'car'
t= 'ab'
flag= True

if len(s)!=len(t):
    print(False)
for i in s:
    if i not in t:
        flag= False
        print(flag)
        
    elif s.count(i) != t.count(i):
        flag= False
        print(flag)
print(flag)
# checkAnagram()