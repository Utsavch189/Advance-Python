import multiprocessing

def calc_square(numbers, result, v):
    """
    Function to compute the square of a list of numbers and store the results in a shared array.
    Also sets a shared value.

    Args:
        numbers (list of int): A list of numbers to be squared.
        result (multiprocessing.Array): A shared array to store the squared results.
        v (multiprocessing.Value): A shared value to be set by this function.
    """
    # Set the shared value to 5.67
    v.value = 5.67
    
    # Compute the square of each number and store the result in the shared array
    for idx, n in enumerate(numbers):
        result[idx] = n * n

if __name__ == "__main__":
    # List of numbers to be squared
    numbers = [2, 3, 5]
    
    # Create a shared array to hold the squared results
    result = multiprocessing.Array('i', 3)
    
    # Create a shared value to be set in the process
    v = multiprocessing.Value('d', 0.0)
    
    # Create a process to run the calc_square function
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v))

    # Start the process
    p.start()

    # Wait for the process to complete
    p.join()

    # Print the shared value
    print(f"Shared value: {v.value}")

    # Print the contents of the shared array
    print(f"Squared results: {list(result)}")
