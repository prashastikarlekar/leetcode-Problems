# Code to implement merge sort algorithm
def mergeSort(A,low,high):
        if low< high:
            mid = int((low+high)/2)        # to divide the array into two halves
            mergeSort(A,low,mid)      # first half of the array
            mergeSort(A,mid+1,high)   # second half of the array
            merge(A,low,mid,high)       # merging those two halves

def merge(A, low, mid, high):
        C = [0] * len(A) # copy of original array
        for i in range(low,high+1): # copies only the elements we got in mergeSort call at their respective indexes, all others are 0
            C[i] = A[i]

        i = low     # first element of thr first array
        j = mid+1   # first element of the second array
        # print(i)
        # print(j)
        for m in range(low, high+1):
            if i>mid:
                A[m]=C[j]
                j+=1
            elif j>high:
                A[m]=C[i]
                i+=1
            elif C[i] <= C[j]: # if element in first array is smaller then in second array, copy element from first array
                A[m] = C[i]
                i+=1    # increment index for thr first array
            else :
                #C[i] > C[j]: # if the element from the second array is smaller than the element from the first array, copy second array element
                A[m] = C[j]
                j+=1    # increment index for the second array
            # now the only cases remaining are when one of the halves is fully copied and other half has remaining elements to be copied
            # elif i>mid :# if i gets incremented upto a level where it is higher than mid, that means first half is fully copied and \
            # # second half has remaining elements to be copied
            #     A[m] = C[j] # so we copy the elements fromt he second half
            #     j+=1 # and increment the pointer for the second half array
            # else: # this will happen when first half elements are fully copied and second half elements are still remaining
            #     # so j becomes greater than high and therefore we stop copying it and copy the remaining elements from the first half
            #     A[m] = C[i]
            #     i+=1

   

if __name__ == "__main__":
    A= [8,9,1,2]
    print("The original array is :")
    [print(i, end = " ") for i in A]
    mergeSort(A,0,len(A)-1)
    print("\n")
    print("The sorted array is : ")
    [print(i, end = " ") for i in A]

    
            




