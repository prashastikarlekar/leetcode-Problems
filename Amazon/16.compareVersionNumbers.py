# Given two version numbers, version1 and version2, compare them.
# Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros.
# Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision
# 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

# To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring 
# any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an 
# index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but
# their revision 1s are 0 and 1 respectively, and 0 < 1.

# Return the following:
# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.

def compareVersions(version1,version2):
    versions1 = (version1.split('.'))
    versions2= (version2.split('.'))
    if len(versions1) < len(versions2):
        difference = len(versions2) - len(versions1)
        [versions1.append('0') for i in range(difference)]
    elif len(versions1) > len(versions2):
        difference = len(versions1) - len(versions2)
        [versions2.append('0') for i in range(difference)]

    i=1
    if versions1[0]<versions2[0]:
        return -1
    elif versions1[0]>versions2[0]:
        return  1
    else:
        while i<len(versions1):
            versions1[i]  = versions1[i].lstrip('0')
            print(versions1[i])
            versions2[i]  = versions2[i].lstrip('0')
            print(versions2[i])
            if versions1[i] < versions2[i]:
                return -1
            elif versions1[i] > versions2[i]:
                return 1
            else:
                
                i+=1
        return 0

if __name__=="__main__":
    # version1 = "1.01"
    # version2 = "1.001"
    # version1 = "1.0"
    # version2 = "1.0.0"
    version1 = "0.1"
    version2 = "1.1"
    print(compareVersions(version1,version2))


