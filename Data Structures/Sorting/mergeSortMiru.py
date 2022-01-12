import timeit
import random
import functools
import matplotlib.pyplot as plt

def mergeSort(arr, low, high):
    if low < high:
        mid = int((low+high)/2)
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):

    i = low
    j = mid+1

    new_queue = Queue()

    for k in range(low, high+1):
        if i > (mid):
            new_queue.append(arr[j])
            j += 1
        elif j > high:
            new_queue.append(arr[i])
            i += 1
        elif (arr[i].val <= arr[j].val):
            new_queue.append(arr[i])
            i += 1
        else:
            new_queue.append(arr[j])
            j += 1

    current = new_queue.getFront()
    for w in range(low,high+1):
        arr[w] = current
        current = current.next
        

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue():
    def __init__(self, node = None):
        self.head = Node(-1)
        self.current = self.head    
        if(node):
            self.head.next = node
            self.current = node
        
    
    def append(self, node):
        node.next= None
        self.current.next = node
        self.current = self.current.next

    def getFront(self):
        return self.head.next

    def printQueue(self):
        current = self.head.next
        print("---------------")
        while(current):
            print(current.val,end=" ")
            current = current.next
        print("\n---------------")



if __name__ == "__main__":
    numberOfElements = int(input("Enter the number of elements: "))
    collection = []
    for i in range(numberOfElements):
        element = int(input("Enter the element: "))
        collection.append(Node(element))
    
    mergeSort(collection, 0, numberOfElements-1)
    
    queue = Queue(collection[0])
    queue.printQueue()
    

# Testing the function


# Testing different input values
print("Testing different inputs for Merge Sort results:")

# Size 1
collection = [1]
numberOfElements = len(collection)

t = timeit.Timer(functools.partial(mergeSort,collection,0,numberOfElements -1))
time_taken = t.timeit(10)
f1_time = time_taken/10

print("Case: Input Size 1 running time was {0}".format(f1_time))


# Unsorted Basic integers
new_collection = []
# numberOfElements   =1000 
numberOFElements = random.sample(range(100000, 1000000), 10)
for x in range(numberOfElements):
    new_collection.append(Node(random.randint(0,1000)))

print("Input:")
for item in new_collection:
    print(item.val,end=" ")


t = timeit.Timer(functools.partial(mergeSort,new_collection,0,numberOfElements-1))
time_taken = t.timeit(10)
f1_time = time_taken/10
print("Output:")
# print(B1)
queue = Queue(new_collection[0])
queue.printQueue()
print("Case: Unsorted Small Basic integers running time was {0}".format(f1_time))
