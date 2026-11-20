# We can make our program decently faster without using threading and multiprocessing. This could be done using asynchronous programming (asyncio)

# say we have to send multiple http requests or download multiple files or access multiple web pages, these tasks could be sped up without multithreading or multiprocessing using asyncio

# there are few concepts in this:
# 1. async def (using async before def declares a coroutine (special function that can be paused))
# 2. await (Pauses execution until the result is ready (waiting but in non blocking fashion))
# 3. asyncio (Built in python library)
# 4. event loop (The engine that runs and schedule co-routines in python) (check pictures on web to understand)



import asyncio

async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(3) # await -> Suspends the current coroutine until the awaited operation completes.
    print("Chai is ready")


# one of the way to run coroutine (more are explored in next files...)
asyncio.run(brew_chai()) # Starts the event loop and runs the main coroutine.