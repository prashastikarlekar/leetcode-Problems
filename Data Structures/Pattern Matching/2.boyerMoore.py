# Boyer moore algorithm for returning the non-overlapping occurences of a pattern in a string 


def find_boyer_moore(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    i = m-1
    k = m-1
    comparisons = 0
    while i < n:
        # If match , decrease i,k
        comparisons+=1 # this is the number of comparisons

        if T[i] == P[k]:
            if k == 0:
                return i
                # j = last.get(T[i], -1)
                # i += m - min(k, comparisons)
                # uncomment below 2 and comment above 2 for getting non-overlapping occurences
                # i += m+ last[T[i]]+1
                # k = m-1

            else:
                i -= 1
                k -= 1
        # Not match , reset the positions
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)
            k = m-1
    
    return comparisons
    # return -1


if __name__=="__main__":
    # T="cdcdcdcdc"
    # P="cdc"
    T= "GCATGACTGCGTGACC"
    P="CTGC"
    print(find_boyer_moore(T,P))