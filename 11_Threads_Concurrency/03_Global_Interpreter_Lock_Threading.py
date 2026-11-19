# when two or more threads try to access something in memory at the same time, the question arises which thread should make the change, in such cases we use mutex (mutex allows us to handle race conditions)

# In standard CPython (the most commonly used Python implementation), the GIL is a lock that ensures only one thread at a time executes Python bytecode within a particular interpreter.

# Why does Python have it?

# Primarily, it simplifies memory management and protects CPython's internal data structures, particularly its reference-counting mechanism.

# Think of it as a single token:
# - A thread must hold the GIL to execute Python bytecode.
# - When one thread holds it, another thread cannot execute Python bytecode simultaneously.
# - Threads can take turns holding the GIL.

import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for i in range(100_000_000):
        count += 1

    print(f"{threading.current_thread().name} finished brewing...")


thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"Total time taken is: {end - start: .2f} seconds")



# Does GIL affect every operation?
# No! This is an important distinction.

# Consider downloading two files.

import threading
import requests

def download_file(url):
    response = requests.get(url)
    print(f"Downloaded: {url}")

t1 = threading.Thread(target=download_file, args=("https://example.com",))
t2 = threading.Thread(target=download_file, args=("https://python.org",))

t1.start()
t2.start()

t1.join()
t2.join()

# When a thread waits for a network response, it generally releases the GIL, allowing another thread to execute Python code.

# This is why multithreading works very well for I/O-bound tasks despite the GIL.