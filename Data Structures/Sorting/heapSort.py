def max_heapify(A,i,heap_size):
    l = 2* i +1
    r = 2* i +2
    largest = i
    if l< heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest !=i:
        A[i],A[largest] = A[largest], A[i]
        max_heapify(A,largest,heap_size)


def build_max_heap(A):
    x= int(len(A)-2/2)
    while(x>=0):
        max_heapify(A,x,len(A))
        x-=1

def heapSort(A):
    build_max_heap(A)
    i= len(A) -1
    while(i>0):
        A[0],A[i]= A[i], A[0]
        max_heapify(A,0,i)
        i-=1


# heap sort algorithm
if __name__=="__main__":
    numberOfElements = int(input("Enter the number of elements: " ))
    inputList =[]
    for i in range(numberOfElements):
        element = int(input("Enter the element: "))
        inputList.append(element)
    print("The input list is :", end=" ")
    [print(i, end=" ")  for i in inputList]
    heapSort(inputList)
    print("\n")
    print(inputList)