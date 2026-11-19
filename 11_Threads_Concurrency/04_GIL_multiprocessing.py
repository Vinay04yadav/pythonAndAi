# Multiprocessing: Multiple workers in separate processes, each with its own GIL. They can execute Python bytecode simultaneously.

# That's why multiprocessing is taking less time than multithreading.

from multiprocessing import Process
import time

def crunch_number():
    print(f"Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1

    print(f"Ended the count process...")


if __name__ == "__main__":
    start = time.time()
    p1 = Process(target = crunch_number)
    p2 = Process(target = crunch_number)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time taken: {end - start: .2f} seconds")


# The GIL is not a restriction on how many threads you can create. It's a restriction on how many threads can execute Python bytecode simultaneously within one standard CPython interpreter.



# Heavy mathematical calculations	-> Multiprocessing
# Image/video processing	-> Multiprocessing
# Multiple API requests -> Multithreading / asyncio
# Downloading multiple files -> Multithreading / asyncio
# File operations	-> Multithreading / asyncio




# NOTE
# __name__ == "__main__" checks whether the Python file is being executed directly.
# In multiprocessing, each child process starts a separate Python interpreter.
# With the spawn method, the child imports the main module to access the target function.
# Without the main guard, process-creation code could execute again during this import,
# potentially causing repeated process creation.
# Therefore, it is good practice to always use the main guard with multiprocessing.