from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
# result=[]
# for i in range(len(strs)):
#     for j in range(i+1,len(strs)):
#         flag=True
#         if len(strs[i])!=len(strs[j]):
#             flag= False
#             continue
#         for k in strs[i]:
#             if k not in strs[j]:
#                 flag= False
#                 continue
#             if strs[i].count(k)!= strs[j].count(k):
#                 flag= False
#                 continue
#         if flag:
#             if result==[]:
#                     result.append([strs[i],strs[j]])
#             for x in result:
#                 # print(x)
#                 if strs[i] in x : 
#                     if strs[j] not in x:
#                         x.append(strs[j]) 
#                 elif strs[j] in x :
#                     if strs[i] not in x:
#                         x.append(strs[i]) 
#                 else:
#                     result.append([strs[i],strs[j]])
# print(result)

answer = defaultdict(list)
# print(answer.values())    # []
for s in strs:
    print(tuple(sorted(s)))
    answer[tuple(sorted(s))].append(s)

print(answer)


s1 = "cba"
print(tuple(sorted(s1)))