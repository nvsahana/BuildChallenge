import threading
import time
from collections import deque

# Producer-Consumer implementation with blocking queue

''' Idea behind the code:
Producer (trying to put())        Consumer (running get())
1. Acquire lock 
2. Check: queue full? Yes
3. wait(): Release lock, Sleep     
---------------------------------4. Acquire lock 
---------------------------------5. Check: queue empty? No
---------------------------------6. popleft(): queue now has space
---------------------------------7. notify_all(): Wake Producer
---------------------------------8. Release lock
9. Wake up, re-acquire lock 
10. Re-check: queue full? NO
11. append(item)
12. Release lock'''

class BlockingQueue:
    def __init__(self, max_size=10):
        self.queue = deque()
        self.max_size = max_size
        self.condition = threading.Condition()

    def put(self, item):
        with self.condition:
            while len(self.queue) >= self.max_size: #always check conditions before proceeding
                self.condition.wait()
            self.queue.append(item)
            self.condition.notify_all()

    def get(self):
        with self.condition: #thread safe with locks (internally creates mutex)
            while len(self.queue) == 0:
                self.condition.wait()
            item = self.queue.popleft()
            self.condition.notify_all()
            return item


class Producer(threading.Thread):
    def __init__(self, source, queue):
        super().__init__()
        self.source = source
        self.queue = queue

    def run(self):
        for item in self.source:
            self.queue.put(item)
            time.sleep(0.01)  # simulate some work


class Consumer(threading.Thread):
    def __init__(self, queue, destination):
        super().__init__()
        self.queue = queue
        self.destination = destination

    def run(self):
        while True:
            item = self.queue.get()
            if item is None:  # ceck for stop signal
                break
            self.destination.append(item) #store item
            time.sleep(0.01)


def run_producer_consumer(source):
    queue = BlockingQueue(5)
    destination = []

    producer = Producer(source, queue) #first, create producer thread
    consumer = Consumer(queue, destination)#create consumer thread

    producer.start()#create new thread and run(), this  executles concurrently with the main
    consumer.start()#start consumer in new thread

    producer.join()
    
    # signal consumer to stop
    queue.put(None)
    consumer.join()

    return destination
