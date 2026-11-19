import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for i in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]

[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final value of counter: {counter}")



# The lock here ensures that only one thread at a time can access and modify the shared variable counter inside the protected section.
# The with lock statement ensures that:
# 1. A thread must acquire the lock before entering the block.
# 2. If another thread already holds the lock, it must wait.
# 3. Once the first thread exits the block, the lock is released.
# 4. Another waiting thread can acquire it.

# What problem does it prevent?
# Consider what could happen without a lock:

# Suppose counter = 10.

# Two threads try to increment it:
# Thread 1	Thread 2
# Reads counter = 10	
# 	Reads counter = 10
# Adds 1 → 11	
# 	Adds 1 → 11
# Writes 11	
# 	Writes 11

# Expected result: 12

# Actual result: 11

# This is called a race condition.

# With a lock, Thread 2 cannot enter the critical section until Thread 1 finishes updating the counter.