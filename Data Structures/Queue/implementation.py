# code to implement a queue
class Queue:

    # the __init__ function to initialize the queue object properties
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear= capacity -1
        self.queue = [None] * capacity
        self.capacity =capacity
    
    def isFull(self):
        # the queue is full if the size of the queue is equal to the capacity of the queue
        return (self.size == self.capacity) 
    def isEmpty(self):
        # the queue will be empty when size =0
        return (self.size == 0)
    
    # Function to add an item to the queue
    # it changes the rear and the size
    def enqueue(self, item) : # it takes the queue and the item to be added
        # first we check before adding if the the queue is already full or not, if yes then we do nothing
        if (self.isFull()):
            print("The queue is full.")
            return
        # if it is not full, we add the item to the queue
        self.rear = (self.rear + 1)% self.capacity # find the index i.e rear where the item will be inserted
        self.queue[self.rear] = item # add the item to the queue
        self.size +=1 # increment the size of the queue
        print(f"Enqueued {item} to the queue. ")
    
    # Function to remove an item from the queue
    # this will change the front and the size of the queue
    def dequeue(self):
        # first we check if the queue is already empty, if so then we dont have anyhting to remove from the queue
        if (self.isEmpty()):
            print("The queue is empty.")
            return
        # if its not empty, we will remove the item present at the front of the queue
        # firstly get the item at the queue
        item = self.queue[self.front]
        self.front = (self.front + 1)%self.capacity # change the front of the queue
        self.size -=1 # decrement the size of the queue
        print(f"Dequeued {item} from the queue. ")
        return item # return the item that was removed from the queue

    # function tot he get the item at te front of the queue
    def getFront(self):
        if self.isEmpty():
            return
        print(f"The element at the front of the queue is {self.queue[self.front]}")
        

    # function to return the rear of the queue
    def getRear(self):
        print(f"The element at the rear of the queue is {self.queue[self.rear]}")
    
    # Function to print the elements of the queue
    def getQueue(self):
        for i in self.queue:
            print(i, end =" ")
        print("\n")


if __name__== "__main__":
    queue = Queue(5)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.getQueue()
    queue.dequeue()
    queue.getFront()
    # queue.getQueue()




