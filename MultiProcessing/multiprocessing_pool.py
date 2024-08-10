from multiprocessing import Pool

def f(n):
    """
    Function to compute the square of a number.

    Args:
        n (int): The number to be squared.

    Returns:
        int: The square of the input number.
    """
    return n * n

if __name__ == "__main__":
    # Create a Pool with 3 worker processes
    p = Pool(processes=3)

    # Map the function 'f' to the list of numbers [1, 2, 3, 4, 5]
    result = p.map(f, [1, 2, 3, 4, 5])

    # Close the pool to prevent any more tasks from being submitted
    p.close()

    # Wait for the worker processes to exit
    p.join()

    # Print the results
    for n in result:
        print(n)


# Example 1: Using apply to Submit a Single Task

from multiprocessing import Pool

def cube(n):
    return n * n * n

if __name__ == "__main__":
    p = Pool(processes=3)
    
    # Apply function to a single argument and get the result
    result = p.apply(cube, (3,))  # Compute the cube of 3
    
    p.close()
    p.join()
    
    print(result)  # Output: 27

# Example 2: Using apply_async for Asynchronous Task Submission

from multiprocessing import Pool

def double(n):
    return n * 2

if __name__ == "__main__":
    p = Pool(processes=3)
    
    # Apply function asynchronously and get a result object
    result = p.apply_async(double, (5,))
    
    # Get the result from the result object
    print(result.get())  # Output: 10
    
    p.close()
    p.join()

# Example 3: Using starmap for Multiple Arguments

from multiprocessing import Pool

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    p = Pool(processes=3)
    
    # Use starmap to apply function with multiple arguments
    result = p.starmap(multiply, [(2, 3), (4, 5), [6, 7]])
    
    p.close()
    p.join()
    
    print(result)  # Output: [6, 20, 42]

"""
Summary:

Pool: Provides a pool of worker processes for parallel processing.
map: Applies a function to each item in an iterable in parallel.
apply: Submits a single task to the pool and waits for the result.
apply_async: Submits a single task asynchronously and retrieves the result later.
starmap: Applies a function with multiple arguments to each item in an iterable of argument tuples.
"""