import threading
import time
from collections import deque

# Producer-Consumer implementation with blocking queue

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
        with self.condition: #thread safe with locks
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
            if item is None:  # poison pill to stop
                break
            self.destination.append(item)
            time.sleep(0.01)


def run_producer_consumer(source):
    queue = BlockingQueue(5)
    destination = []

    producer = Producer(source, queue) #first, create producer thread
    consumer = Consumer(queue, destination)

    producer.start()#create new thread and run(), this  executles concurrently with the main
    consumer.start()

    producer.join()
    
    # signal consumer to stop
    queue.put(None)
    consumer.join()

    return destination
