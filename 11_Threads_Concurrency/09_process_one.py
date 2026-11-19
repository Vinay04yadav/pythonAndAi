import threading
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**8):
        total += i
    print("Done")

start = time.time()

threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]

[t.start() for t in threads]
[t.join() for t in threads]

end = time.time()
print(f"Time taken by two threads is: {end - start : .2f} seconds")

# Taking almost 5 seconds, check file 10 for better code ( multiprocessing happening there )