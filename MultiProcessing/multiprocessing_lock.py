import time
import multiprocessing

def deposit(balance, lock):
    """
    Deposits money into the shared balance.

    Args:
        balance (multiprocessing.Value): The shared balance value.
        lock (multiprocessing.Lock): A lock to synchronize access to the balance.
    """
    for i in range(100):
        time.sleep(0.01)  # Simulate time taken to deposit money
        lock.acquire()  # Acquire the lock before accessing the balance
        balance.value = balance.value + 1  # Increment the balance
        lock.release()  # Release the lock after updating the balance

def withdraw(balance, lock):
    """
    Withdraws money from the shared balance.

    Args:
        balance (multiprocessing.Value): The shared balance value.
        lock (multiprocessing.Lock): A lock to synchronize access to the balance.
    """
    for i in range(100):
        time.sleep(0.01)  # Simulate time taken to withdraw money
        lock.acquire()  # Acquire the lock before accessing the balance
        balance.value = balance.value - 1  # Decrement the balance
        lock.release()  # Release the lock after updating the balance

if __name__ == '__main__':
    # Create a shared balance value with an initial amount of 200
    balance = multiprocessing.Value('i', 200)

    # Create a lock to synchronize access to the shared balance
    lock = multiprocessing.Lock()

    # Create and start the deposit process
    d = multiprocessing.Process(target=deposit, args=(balance, lock))
    d.start()

    # Create and start the withdraw process
    w = multiprocessing.Process(target=withdraw, args=(balance, lock))
    w.start()

    # Wait for both processes to complete
    d.join()
    w.join()

    # Print the final balance after both processes have finished
    print(f'Final balance: {balance.value}')
