# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# logs = ["t kvr", "r 3 1", "i 403", "7 so", "t 54"]
# logs =["j je", "b fjt", "7 zbr", "m le", "o 33"]
logs=["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

# all digi logs- where all words contain a digit, come at the end and maintain their relative order in the output
# Letter-logs: All words (except the identifier) consist of lowercase English letters.
#1. Identify whether the current log is digit log or letter log
identifier = ""
i,j=0,0
letterLogs, digitLogs = [],[]
for i in logs:
    if i.split()[1].isdigit():
        digitLogs.append(i)
    else:
        letterLogs.append(i)
print(letterLogs)
print(digitLogs)
# letterLogs.sort(key = lambda x: map.keys() if sameValue(x.split()[1:]) else map.values())
#split(" ", 1) # here 1 is the maxsplit which is a number that tells how many times can a string be splited 
# so if we split the string max 1 times- identifier will be seperated from the rest and this x.split(' ', 1)[1] fetches the rest part
letterLogs.sort(key=lambda x: (x.split(' ', 1)[1], x)) 
# we use this tuple in the key of sort() when we have to sort on multiple basis- first preference is rest part and if its same - sort
# them on the basis of actual log that is starting from the 0th index
print(letterLogs)
"kj".split()

# old approach when i thought every word in digit log should be checked if it is a digit but we only need to check if the second word 
# is digit and we can call it digit log if it is digit

# while i< len(logs):
#     # print(logs[i][j])x
#     if logs[i][j] == " ":
#         identifier= logs[i][:j]
#         identifier_length = len(identifier)
#         # print(letterLogs)
#         # print(f"The identifier is {identifier} and length is {len(identifier)}")  
#         print( logs[i][identifier_length+1:])
#         # if any(letterLogs[identifier_length+1:])
#             # sameWords+=1
#         for k in logs[i][identifier_length+1:]:
#             flag = True
#             # print("".join(k))
#             if not k.isdigit() and k!=" ":
#                 flag = False # this means its a letter log
#             if k in letterLogs[identifier_length+1:]:
#                 sameWords+=1
#         if flag and logs[i] not in digitLogs:
#             print(f"The log {logs[i]} is digit log") 
#             digitLogs.append(logs[i])
#         elif not flag and logs[i] not in letterLogs:
#             letterLogs.append(logs[i])
#             print(f"The log {logs[i]} is a letter log")
#         i+=1
#         j=0
#     else:
#         j+=1

# print(letterLogs)  
# print(sameWords)
# letterLogs.sort(key = lambda x: x.split()[1:] if not (ele == x.split()[1] for ele in letterLogs) else x.split()[0]) 
# print(f"The letter logs are {letterLogs} and the digit logs are {digitLogs}")
# print(letterLogs+digitLogs)
