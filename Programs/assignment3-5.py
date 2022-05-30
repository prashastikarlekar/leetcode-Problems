import time
from random import randint as rn
# import matplotlib.pyplot as plt

def algorithm1( S):
    #S:sequence
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
            return True
        
def algorithm2(S):
    #S:sequence
    S = sorted(S)
    for j in range(1, len(S)):
        if S[j-1] == S[j]:
            return False
        return True
    
def algorithm3(S, start, stop):
    #slice S[start:stop], S:sequence
    if stop - start <= 1: return True
    elif not algorithm3(S, start, stop-1): return False
    elif not algorithm3(S, start+1, stop): return False
    else: return S[start] != S[stop-1]
    
def max(totalTime):
    if totalTime > largestInput:
        totalTime = largestInput
        return totalTime
    
inputSize = rn(1,10)  # randomly generated input size
S = [rn(1,11) for i in range(inputSize)]   # randomly generated list 
largestInput = 0
    
for j in range(1,1000):
#     inputSize.append(rn(1,j))
    startTime = time.time()
    algorithm1(S)
    endTime = time.time()
    elapsedTime = endTime -startTime
    if elapsedTime >= 45:
        pass
    else:
        maximumTime = max(elapsedTime)
        maximumInput = int(len(S))
    
print(maximumInput)
