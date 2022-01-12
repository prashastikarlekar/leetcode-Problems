# Applied Algo assignemnt
# Implement a bottom-up merge-sort for a collection of items by placing each item in its ownqueue, and then repeatedly merging pairs of
#  queues until all items are sorted within a single queue.

class Queue:
    def __init__(self, capacity):
        self.size = 0
        self.front = self.size = 0
        self.rear = capacity -1
        self.queue = [None] * capacity
        self.capacity = capacity

    def isEmpty(self):
        return (self.size ==0)
    def isFull(self):
        return (self.size == self.capacity)
    
    def getFront(self):
        print(f"The element at the front of the queue is {self.queue[self.front]}.")
    def getRear(self):
        print(f"The element at the rear of the queue is {self.queue[self.rear]}.")
    def getQueue(self):
        for i in self.queue:
            print(i, end=" ")
        print("\n")

    def enqueue(self, item):
        if self.isFull():
            print("The queue is full.")
        self.rear = (self.rear + 1)%self.capacity
        self.queue[self.rear] = item
        self.size +=1
        print(f"Enqueued {item} to the queue.")

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty.")
        self.front = (self.front + 1)% self.capacity
        item = self.queue[self.front]
        self.size -=1
        print(f"Dequeued {item} from the queue.")


def mergeSort(A, low, high): 
    if low< high:
        mid = int((low+high)/2) # calculate the mid of the queue and divide the queue in two halves
        mergeSort(A, low, mid) # divide the left queue recursively
        mergeSort(A, mid+1, high) # divide the right half recursively
        merge(A,low, mid, high) # merge the solutions of the two halves

def merge(A, low, mid, high):
    # first we create a dummy array to store the elements that we are merging in this iteration
    C = Queue(numberOfElements)
    for i in range(low, high+1):
        C.enqueue(A.getFront())
    
    # now we create a pointer to track the lef half of the queue
    i = low # this is the lowest index of the left half queue
    # and another pointer to track the right ha;f of the queue
    j = mid+1 # this is the lowest index of the right half of the queue
    
    for m in range(low,high+1):
        if i> mid: # this means that the elements from the left half are already copied to the original array and the remaining 
            # elements are left from the right half of the queue
            A[m] = C[j] # copy the elements from the right half of the queue
            j+=1 # increment the pointer for the right half
        elif j> high:
            # this means that the elements from the right half of the queue are fully copied and the only elements remaining are from
            # the left half of the queue, so we now copy them to the original array
            A[m] = C[i]
            i+=1
        elif C[i] <= C[j]:
            # if the element in the left half of the queue is smaller or equal to the lement in the righ thalf of the queue
            # then we copy the element from the left half of the queue
            A[m] = C[i]
            i+=1 # and increment the pointer for the left half of the queue
        else:
            # if all the conditions are not true that means that C[j] < C[i]
            # i.e the element in the right half of the queue is smaller than the one in the left half
            A[m] = C[j]
            j+=1

if __name__ == "__main__":
    numberOfElements = int(input("Enter the number of elements in the queue: "))
    queue = Queue(numberOfElements)
    for i in range(numberOfElements):
        element = int(input("Enter the element: "))
        queue.enqueue(element)
    queue.getQueue()
    mergeSort(queue, 0, numberOfElements-1)


    
