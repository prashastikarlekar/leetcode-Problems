# x= -123
# x=1534236469
# x= -2147483412
x=120
abs_x= abs(x)
# calculate length of the integer
length_x= len(str(abs_x))
print(length_x)

listOfReverseDigits= []
if x<0:
    listOfReverseDigits.append('-')
for i in range(length_x):
    n=abs_x%10
    abs_x=abs_x//10
    print(n)
    listOfReverseDigits.append(n)
    
print(listOfReverseDigits)

stringNumber= [str(i) for i in listOfReverseDigits]
print(stringNumber)
result= int("".join(stringNumber))
if not(result >= -(2**31) and result <=(2**(31)-1)):
    print("0: Doesnot fall in the range")
print((result))
print(result <=(2**(31)-1))