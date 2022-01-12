# dynamic approach
def longestCommonSubsequence(A,B):
    m=len(A)
    n=len(B)
    L=[[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif A[i-1]==B[j-1]:
                L[i][j] = 1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])

    return L[m][n]

if __name__=="__main__":
    A= "AGGTAB"
    B="GXTXAYB"
    print(longestCommonSubsequence(A,B))

