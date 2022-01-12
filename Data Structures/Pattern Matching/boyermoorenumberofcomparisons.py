def find_boyer_moore(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    i = m-1  
    k = m-1
    count=0
    while i < n:
        # If match , decrease i,k
        if T[i] == P[k]:
            if k == 0:
                return [i,count]
            else:
                i -= 1
                k -= 1
# Not match , reset the positions
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)
            k = m-1
        count+=1
    return -1

if __name__=="__main__":
    T= "abacaabaccabacabaabb"
    P="abacab"
    print(find_boyer_moore(T,P))