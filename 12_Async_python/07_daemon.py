# daemon threads are the background threads which automatically shut down when the main program exit.

# these are used for non critical background tasks like logging, monitoring etc

import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...\n")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main program done")

# above program will print "Monitoring tea temperature" and instantly goes to "Main program done" and daemon thread is also shut down (during the sleep duration itself)