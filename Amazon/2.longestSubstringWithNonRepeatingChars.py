s="abcabaa"
max_length =0
str_list =[]
for x in s:
    if x in str_list:
        str_list = str_list[str_list.index(x)+1:]
    str_list.append(x)
    max_length=max(max_length,len(str_list))
print(max_length)