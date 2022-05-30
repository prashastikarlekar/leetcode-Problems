# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.
# ransomNote = "aa"
ransomNote ="fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"
# magazine = "aab"
# magazine ='ab'
flag= True
for i in ransomNote:
    if i not in magazine:
        flag = False
        break
    elif magazine.count(i) < ransomNote.count(i):
        flag = False
        print(f'Its false  because  i is {i} ransomnote {ransomNote.count(i)} and magazine {magazine.count(i)}')
        # continue
    
print(flag)
        

# dict1={}
# dict2={}
# for i in ransomNote:
#     if i not in dict1:
#         dict1[i] = ransomNote.count(i)
# print((sorted(dict1.items())))
# for j in magazine:
#     if j not in dict2:
#         dict2[j] = magazine.count(j)
# print(dict2)

# flag = False
# for key1,value1 in dict1.items():
#     for key2,value2 in dict2.items():
#         if key1 not in dict2.keys():
#             print(f'{flag}. key 1 is {key1}')
#             # print('false')
#         # elif key1 == key2:


            
#         #     break
#         # elif key1 == key2:
#         #     if value1 <= value2:
#         #         # print('True')
#                 # flag = True
#                 # break
#             # else:
#                 # print("false")
# print(flag)

        