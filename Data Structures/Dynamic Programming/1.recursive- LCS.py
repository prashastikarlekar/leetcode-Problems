# Recursive approach
def longestCommonSubsequence(A,B,i,j):
    if i==len(A) or j ==len(B):
        return 0
    elif A[i] == B[j]:
        return 1+ longestCommonSubsequence(A,B,i+1,j+1)     
    else:
        return max(longestCommonSubsequence(A,B,i+1,j),longestCommonSubsequence(A,B,i,j+1))
    

if __name__=="__main__":
    A="bd"
    B="abcd"
    print(longestCommonSubsequence(A,B,0,0))
