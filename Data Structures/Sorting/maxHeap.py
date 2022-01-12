def max_heapify(A,i):
    l = 2* i +1
    r = 2* i +2
    input_length = len(A)
    heap_size = input_length
    if l<= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r] > A[i]:
        largest = r
   
    if largest !=i:
        A[i],A[largest] = A[largest], A[i]
        max_heapify(A,largest)

def build_max_heap(A):
    input_length = len(A)
    heapSize = input_length
    for i in range(int(input_length/2), 0,-1):
        max_heapify(A,i)

def heapSort(A):
    build_max_heap(A)
    input_length = heapSize =  len(A) 
    
    for i in range(input_length, 1 ,-1):
        A[1],A[i]= A[i], A[1]
        heapSize -=1
        max_heapify(A,1)
        


# heap sort algorithm
if __name__=="__main__":

    A= [3,2,14,6,2,7,9]
    heapSort(A)
    print(A)
    

