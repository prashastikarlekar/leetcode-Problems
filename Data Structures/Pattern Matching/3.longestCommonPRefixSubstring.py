# Given a text D and a pattern P, describe an Ω(d+p) time method for finding the longest prefix
# of P that is a substring of D. The lengths of D and P are d and p, respectively.
def longestPrefixSubstring(D,P):
    n=1
    result =''
    for i in range(len(P)):
        index = D.index(P[:n])
        if index!= -1:
            result+= P[:n]
        n+=1
    return result

if __name__=="__main__":
    D= "hellohihello"
    P="ihellr" # answer should be ihell
    # print(longestPrefixSubstring(D,P))
    print(D.index(P[1:2]))