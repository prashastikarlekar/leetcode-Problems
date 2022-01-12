# Brute force
def find_brute(T, P):
    n, m = len(T), len(P)
    # output =[]
    count=0
    # every starting position
    for i in range(n-m+1):
        k = 0
        
    # conduct O(k) comparisons
        while k < m and T[i+k] == P[k]:
            k += 1
            count+=1
        count+=1

        if k == m:
            return [i,count-1] # index and numbe rof comparisons
    return -1

if __name__=="__main__":
    T= "abacaabaccabacabaabb"
    P="abacab"
    print(len(P))
    print(find_brute(T,P))