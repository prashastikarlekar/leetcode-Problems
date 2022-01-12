# code to implement count sort
input =[9,6,3,5,3,4,3,9,6,4,6,5,8,9,9]


minElement = min(input)
maxElment = max(input)
rangeOfElements = maxElment- minElement + 1
frequencyArray = [0] * rangeOfElements

for i in input:
    representativeIndex = i - minElement
    frequencyArray[representativeIndex] +=1
print(frequencyArray)   #[3, 2, 2, 3, 0, 1, 4]

prefixSumArray = frequencyArray 
start = prefixSumArray[0] 
for i in range(1,len(prefixSumArray)):
    prefixSumArray[i]+= start
    start = prefixSumArray[i]
print(prefixSumArray)

for i in range(len(prefixSumArray)):
    prefixSumArray[i]-= 1
print(prefixSumArray)

output =[0]*len(input) 

for i in range(len(input)-1,-1,-1):
    representativeIndexInPrefixSumArray = input[i]- minElement
    output[prefixSumArray[representativeIndexInPrefixSumArray]] = input[i]
    prefixSumArray[representativeIndexInPrefixSumArray]-= 1

print(output)