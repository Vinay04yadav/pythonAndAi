# ==========================================
# CONCURRENCY VS PARALLELISM
# ==========================================

# 1. CONCURRENCY
# Multiple tasks make progress during overlapping periods.
# Tasks can switch between each other instead of running simultaneously.
# Example: While one API request is waiting for a response,
# Python can work on another API request.

# Python tools: asyncio, threading (threading.Thread)

# Example:
# import asyncio

# async def task(name):
#     print(f"{name} started")
#     await asyncio.sleep(2)
#     print(f"{name} completed")

# async def main():
#     await asyncio.gather(
#         task("Task 1"),
#         task("Task 2"),
#         task("Task 3")
#     )

# asyncio.run(main())

# Where to use:
# - Multiple API requests
# - Downloading multiple files
# - Web servers handling multiple users
# - I/O-bound tasks (waiting for network, files, etc.)


# 2. PARALLELISM
# Multiple tasks execute at the exact same time.
# Usually achieved using multiple CPU cores.
# Example: Two processes performing mathematical calculations
# simultaneously on different CPU cores.

# Python tool: multiprocessing (multiprocessing.Process, concurrent.futures.ProcessPoolExecution)

# Example:
# from multiprocessing import Pool

# def square(n):
#     return n * n

# if __name__ == "__main__":
#     with Pool() as pool:
#         results = pool.map(square, [1, 2, 3, 4, 5])
#         print(results)

# Output: [1, 4, 9, 16, 25]

# Where to use:
# - Image/video processing
# - Large mathematical computations
# - Data processing
# - CPU-intensive tasks


# ==========================================
# KEY DIFFERENCE
# ==========================================

# Concurrency -> Managing multiple tasks with overlapping execution.
# Parallelism -> Executing multiple tasks simultaneously.

# Concurrency -> asyncio, threading
# Parallelism -> multiprocessing

# NOTE:
# Python's GIL generally prevents multiple threads from executing
# Python bytecode simultaneously in standard CPython builds.
# Multiprocessing is commonly used for CPU-bound parallelism.





import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order for #{i} customer")
        time.sleep(1) 

# why would you make a program sleep?

# Avoid overwhelming servers: When making multiple API requests, we may introduce delays to avoid hitting rate limits.
# Wait for something: Give a file download, external service, or another operation time to complete.
# Retry mechanisms: If an API request fails, wait a few seconds before trying again.
# Periodic tasks: Run something at fixed intervals, like checking whether a website is responding every 10 seconds.
# Simulations: Simulate real-world delays, such as a machine processing something or a user typing.

def brew_orders():
    for i in range(1,4):
        print(f"Brewing order for #{i} customer")
        time.sleep(2)

# take_orders()
# brew_orders()

# create threads (say we want to seggregate tasks to different threads)

order_thread = threading.Thread(target=take_orders) # simply writing threading.Thread() won't do anything, you have to assign some target function to it which it has to execute.
brew_thread = threading.Thread(target=brew_orders)

# creating threads doesn't mean we have invoked them, we have to start them separately

order_thread.start()
brew_thread.start()

# wait for both to finish (without this orders and brewing will be done asynchronously)
order_thread.join()
brew_thread.join()

print(f"All orders taken and brewed")

# In the above example, we are using only one core but multiple threads. the switching between them is quick.




# Sequential: Finish task A, then start task B.
# Concurrent: Start A and B, and manage their progress together.
# Parallel: Actually execute A and B at the same time.