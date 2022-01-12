# Brute force pattern matching algorithm to return the non-overlapping occurences of a pattern in a string 

def bruteForce(T,P):
   
    n,m=len(T),len(P)
    count =0
    i=0
    while i< n-m+1: # i will go till the index jaha tak m length ki string possible hai
        k=0 # pointer to string P
        while k<m:  
            if T[i+k]==P[k]:
                k+=1
            else:
                i+=1
                break
        if k==m:
            count+=1
            i=i+k

            # return i
    return count    

if __name__=="__main__":
    T= "abacaabaccabacabaabb"
    P="abacab"
    # T="cdcdcdcdc"
    # P="cdc"
    print(bruteForce(T,P))




# def find_brute(T, P):
# 3 n, m = len(T), len(P)
# 4 # every starting position
# 5 for i in range(n-m+1):
# 6 k = 0
# 7 # conduct O(k) comparisons
# 8 while k < m and T[i+k] == P[k]:
# 9 k += 1
# 10 if k == m:
# 11 return i
# 12 return -1