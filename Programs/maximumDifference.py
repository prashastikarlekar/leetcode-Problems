# using kadanes algorithm to solve the max profit problem
prices = [7,1,5,3,6,4]
maxDiff = 0
currentDiff =prices[0]
for i in prices:
    # print(i)
    currentDiff = max(0, i - currentDiff )
    print(f'i is {i}, difference is {currentDiff}')
    if currentDiff > maxDiff :
        maxDiff = currentDiff
print(maxDiff)
minDiff = max(int)
print(minDiff)
