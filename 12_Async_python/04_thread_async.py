# asyncio and threading together

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# ThreadPoolExecutor is a Python utility that manages a pool of worker threads and distributes tasks among them.

# Instead of manually creating threads using threading.Thread(), we can submit tasks to the executor, and it handles thread creation, scheduling and reuse.


def check_stock(item): # assume this function makes a query to db, and returns if item avl or not
    print(f"Checking {item} in store...")
    time.sleep(3) # blocking operation
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")
        print(result)

asyncio.run(main())


# asyncio.get_running_loop()
# Gets the currently running event loop.

# ThreadPoolExecutor()
# Creates a pool of reusable worker threads.

# loop.run_in_executor()
# Runs a synchronous/blocking function in a separate executor.

# await
# Suspends the current coroutine until the submitted operation completes.
# Meanwhile, the event loop can execute other tasks.

# time.sleep()
# Blocks the current thread.

# Main purpose:
# Integrate blocking synchronous functions into an asynchronous program
# without blocking the event loop.