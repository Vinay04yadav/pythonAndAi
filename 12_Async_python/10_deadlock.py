import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def task1():
    with lock_a:
        print("Task 1 acquired lock a")
        with lock_b:
            print("Task 1 acquired lock b")


def task2():
    with lock_b:
        print("Task 2 acquired lock b")
        with lock_a:
            print("Task 2 acquired lock a")


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()


# Two threads are created, and each thread needs both locks to complete.
#
# Task 1 acquires lock_a first, then tries to acquire lock_b.
# Task 2 acquires lock_b first, then tries to acquire lock_a.
#
# If Task 1 holds lock_a and Task 2 holds lock_b simultaneously:
# - Task 1 waits for Task 2 to release lock_b.
# - Task 2 waits for Task 1 to release lock_a.
#
# Both threads keep waiting for each other, and neither can proceed.
# This situation is called a DEADLOCK.
#
# The deadlock occurs because the threads acquire locks in opposite orders.