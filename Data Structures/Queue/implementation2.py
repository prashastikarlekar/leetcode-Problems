# practice to implement a queue 
class Queue:
    def __init__(self, capacity):
        self.size = 0
        self.front = self.size = 0
        self.rear = capacity -1
        self.queue = [None] * capacity    
        self.capacity = capacity

    # function to check of the queue is empty
    def isEmpty(self):
        # the queue will be empty if the size =0
        return (self.size ==0)

    # function to check if the queue is full
    def isFull(self):
        # to check if the queue is full, check if the size = capacity
        return (self.size == self.capacity)

    # function to get the element at the front of the queue
    def getFront(self):
        print(f"The element at the front of the queue is {self.queue[self.front]}")
    
    # function to get the lement at the rear of the queue
    def getRear(self):
        print(f"The element at the rear of the array is {self.queue[self.rear]}")

    # function to add the element to the queue
    # this will change the rear and the size of the queue
    def enqueue(self, item): # it will take the item to be added to the queue
        # firstly we check if the queue is already full
        if self.isFull():
            print("The queue is full.") # we donot add an item to the queue if this is true
        # now if the condition is false, we add the item to the queue
        self.rear = (self.rear + 1)%self.capacity # calculate the index i.e rear where te item will be added in the queue
        self.queue[self.rear] =item  # insert the item at the rear
        self.size +=1 # increment the size of t he queue
        print(f"Enqueued {item} to the queue.")

    # function to the remove element from the queue
    # this will change the front and the size of the queue
    def dequeue(self):
        # firstly we check if the queue is empty or not, if it is, we return nothing
        if self.isEmpty():
            print("The queue is empty.")
        # if not we remove the element from the queue
        self.front = (self.front + 1)%self.capacity # calculate the front i.e the index from where we have to remove the item
        item = self.queue[self.front] # get the item to be removed from the queue
        self.size -=1 # decrement the size of the queue
        print(f"Dequeued {item} from the queue.")

    # function to print the elements of the queue
    def getQueue(self):
        for i in self.queue:
            print(i, end =" ")

if __name__ =="__main__":
    queue= Queue(10)
    queue.enqueue(100)
    queue.enqueue(200)
    queue.enqueue(300)
    queue.enqueue(400)
    queue.enqueue(500)
    queue.enqueue(600)
    queue.getQueue()
    queue.getFront()
    print("\n")
    queue.dequeue()
    queue.getFront()
    # queue.getQueue()


