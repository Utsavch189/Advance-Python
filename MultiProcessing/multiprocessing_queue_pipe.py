import multiprocessing

def calc_square(numbers, q):
    """
    Function to compute the square of a list of numbers and place the results in a queue.

    Args:
        numbers (list of int): A list of numbers to be squared.
        q (multiprocessing.Queue): A multiprocessing queue to store the squared results.
    """
    for n in numbers:
        q.put(n * n)  # Compute the square of each number and put it in the queue

if __name__ == "__main__":
    # List of numbers to be squared
    numbers = [2, 3, 5]

    # Create a multiprocessing queue to hold results
    q = multiprocessing.Queue()

    # Create a process to run the calc_square function
    p = multiprocessing.Process(target=calc_square, args=(numbers, q))

    # Start the process
    p.start()

    # Wait for the process to complete
    p.join()

    # Retrieve and print results from the queue
    while not q.empty():
        print(q.get())
