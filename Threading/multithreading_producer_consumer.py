import time
from random import randint
import threading

queue = []
queue_lock = threading.Lock()  # Lock to ensure thread-safe access to the queue

def produce():
    for i in range(5):
        time.sleep(1)
        item = randint(0, 9)
        with queue_lock:
            queue.append(item)
        print(f"Produced: {item}")

def consume():
    while True:
        with queue_lock:
            if queue:
                item = queue.pop(0)
                print(f"Consumed: {item}")
        time.sleep(1)  # Sleep to simulate time taken to consume an item

if __name__ == "__main__":
    p = threading.Thread(target=produce)
    c = threading.Thread(target=consume)

    p.start()
    c.start()

    p.join()  # Wait for the producer thread to finish
    # Optionally, add a mechanism to stop the consumer thread gracefully

"""
Key Points:

Thread-Safe Queue Access: A queue_lock is used to synchronize access to the shared queue, preventing race conditions.
Producer Function: The produce function generates random numbers and appends them to the queue, with a delay of 1 second between each addition.
Consumer Function: The consume function continuously checks the queue, processes items if available, and prints the consumed item. It also sleeps for 1 second between each check.
Thread Management: The produce and consume threads are started and joined to ensure that the main program waits for the producer to complete.
"""