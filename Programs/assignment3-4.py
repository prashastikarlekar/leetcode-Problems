# import pandas as pd
# import matplotlib.pyplot as plt
import random
#create DataFrame
# df = pd.DataFrame({'x': [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
#                          14, 15, 16, 17, 18, 19, 20, 21, 22],
#                    'y': [3, 4, 5, 7, 9, 13, 15, 19, 23, 24, 29,
#                          38, 40, 50, 56, 59, 70, 89, 104, 130]})

# #create scatterplot
# plt.scatter(df.x, df.y)

# def average1(S):
#     # S:sequence
#     n = len(S)
#     my_average = [0]*n
#     for j in range(n):
#         total = 0
#         for i in range(j + 1):
#             total += S[i]
#             my_average[j] = total / (j+1)
#             return my_average

# def average2(S):
#     #S:sequence
#     n = len(S)
#     my_average= [0]*n
#     for j in range(n):
#         my_average[j] = sum(S[0:j+1]) / (j+1)
#     return my_average
        
# def average3(S):
#     #S:sequence
#     n = len(S)
#     my_average = [0]*n
#     total = 0
#     for j in range(n):
#         total += S[j]
#         my_average[j] = total / (j+1)
#     return my_average



li= [1,2,4,4]
print(max(li,[7]))
inputSize = random.randint(1,100)
print(inputSize)
S = [random.randint(1,11) for i in range(inputSize)]
print(S)