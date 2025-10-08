class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)


    def dequeue(self):
        if self.is_empty():
            print("the queue is empty there no item to remove")
            return None
        else:
            item = self.queue.pop(0)
            print("Removed",item)


    def is_empty(self):
        return len(self.queue) == 0
    
    
    def size(self):
        print("the size of queue is :",len(self.queue))


    def display(self):
        print(self.queue)
        

q = Queue()

q.is_empty() 
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
q.size()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.display()

q.is_empty() 

q.size()