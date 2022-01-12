# Code to implement merge sort part 2
def mergeSort(A, low, high):
    if low<high:
        mid = int((low+high)/2)
        mergeSort(A,low, mid)
        mergeSort(A,mid+1,high)
        merge(A, low, mid, high)

def merge(A, low,mid,high):
    # first we will copy the elements that we want to merge from the original array to a dummy array
    C = [1]*len(A)
    for i in range(low,high+1):
        C[i] = A[i]

    # declare a pointer to keep a track on the left array
    i= low # this is the lower end of the left array
    # declare a pointer to keep track on the right array
    j = mid+1 # this is the lower end of the right end

    for m in range(low,high+1):

        if i> mid:
            # this means that left half k saare elements copy ho chuke h
            # and we have to copy the elements from the right half
            A[m] = C[j]
            j+=1
        elif j> high:
            # this means that right half k saare elements are already copied and we have to copy the left half now
            A[m] = C[i]
            i+=1
        elif C[i] <= C[j]:
            # this means the left half element is smaller than the right half element so we have to copy the element from
            # the left array first and increase the pointer for the left half
            A[m] = C[i]
            i+=1
        else:
            # this means the element fromt he right half is smaller than the lement in the left half
            # so we have to copy that before in the original array
            A[m] = C[j]
            j+=1

if __name__=="__main__":
    n= int(input("Enter the number of elements in the array: "))
    originalArray = []
    for i in range(n):
        element = int(input("Enter the element: "))
        originalArray.append(element)
    [print(i, end =" ") for i in originalArray]
    # call merge sort on the original array
    mergeSort(originalArray, 0, n-1)
    print("\n")
    [print(i, end =" ") for i in originalArray]

