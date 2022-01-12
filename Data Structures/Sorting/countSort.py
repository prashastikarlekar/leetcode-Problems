# code to implement count sort
input =[9,6,3,5,3,4,3,9,6,4,6,5,8,9,9]

# first step is to calculate range
minElement = min(input)
maxElment = max(input)
# rangeOfElements = maxElment - minElement
# but here we want to know the number of elements in the frequency array so we do range +1
rangeOfElements = maxElment- minElement + 1
# print(rangeOfElements)    # 7
frequencyArray = [0] * rangeOfElements
# print(frequencyArray) # [0,0,0,0,0,0,0]
# now, the frequency array representation is as follows - 0th index represents minElement and 6th index represents maxElement

# Secondly, loop through the original array and with every occurence of a number, increment its representation index in frequency array with 1
for i in input:
    # how to know representation of original number in frequency array? eg. 6-[9] so for 9- do (9-minElement) = 6th index
    representativeIndex = i - minElement
    frequencyArray[representativeIndex] +=1
print(frequencyArray)   #[3, 2, 2, 3, 0, 1, 4]

# Thirdly, we calculate prefix-sum array
prefixSumArray = frequencyArray # make copy of frequency array
start = prefixSumArray[0] # first element as it is , start from second to calculate all rpefixes
for i in range(1,len(prefixSumArray)):
    prefixSumArray[i]+= start
    start = prefixSumArray[i]
print(prefixSumArray)

# Forthly, to get array of indices, reduce the array elements by 1
for i in range(len(prefixSumArray)):
    prefixSumArray[i]-= 1
print(prefixSumArray)

output =[0]*len(input) 

# Fifth, loop through original array in reverse order
for i in range(len(input)-1,-1,-1):
    representativeIndexInPrefixSumArray = input[i]- minElement
    output[prefixSumArray[representativeIndexInPrefixSumArray]] = input[i]
    prefixSumArray[representativeIndexInPrefixSumArray]-= 1

print(output)