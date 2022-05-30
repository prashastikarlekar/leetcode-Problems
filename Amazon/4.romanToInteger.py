# num ="MCMXCIV"
num='III'
# map= [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
map= {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
result=0
left =0
right =len(num)
while left<right:
    if left<right-1 and num[left:left+2] in map:
        result+=map[num[left:left+2]]        
        left+=2
    elif num[left] in map:
        result+=map[num[left]]
        left+=1
print(result)
