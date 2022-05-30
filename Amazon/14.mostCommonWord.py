import operator,re
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." 
# # print(paragraph.split())
# banned = ["hit"]
# for i in banned:
#     i =i.lower()

# normalised_string = ''.join([i.lower() if i.isalnum() else ' ' for i in paragraph])
# print(normalised_string)
# map= {}
# words= normalised_string.split()
# # for i in range(len(words)):
# #     if words[i].isalnum():
# #         words[i]= words[i].lower()
# #         # words[i]= words[i].replace('.','')
# #         print(words[i]) 
# #     elif words[i].endswith(','):
# #         words[i]=words[i].replace(',','')
# # print(words)
# for i in words:
#     if i in map:
#         map[i]+=1
#     else:
#         if i not in banned:
#             map[i]=1
# print(map)
# # print(max(map.values()))
# # for i in map.keys():
# #     if map[i] ==max(map.values()):
# #         print(i)

# print(max(map.items(),key = operator.itemgetter(1))[0])
# if i write itemgetter(0) it will sort according to the key and not the values

# re.sub(pattern to be replaced, replaced with that?, string to be searched)

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# paragraph="a, a, a, a, b,b,b,c, c"
# banned= ["a"]
# banned = ["hit"]
paragraph ="Bob. hIt, baLl"
banned=["bob", "hit"]
map={}
# for i in paragraph.split(','):
paragraph= paragraph.lower()
paragraph = re.sub(r"[!,.';?]+"," ",paragraph)
for i in paragraph.split() :
    print(i)
    # i=(re.sub(r'[^\w\s+]','',i)).lower().strip()
    if i in map:
        map[i]+=1
    elif i not in map and i not in banned :
        map[i]=1
print(map)
print(max(map.items(),key = operator.itemgetter(1)))