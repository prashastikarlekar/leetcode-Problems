s='[]()'
stack =[]
map = {']':'[','}':'{',')':'('}
for i in s:
    if i in map:
        top = stack.pop() if stack else ' '
        if map[i]!= top:
            print(False)
    else:
        stack.append(i)
print(not stack)