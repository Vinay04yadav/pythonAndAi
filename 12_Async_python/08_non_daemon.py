import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...\n")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp)
t.start()

print("Main program done")


# Main program done but tea temperature will keep on being monitored :) since it's not daemon thread.

# Profiling: profiling in python is basically seeing how much time which function, method, co-routine took etc. 
# while running file: run in this way for profiling: python -m cProfile -s time file_name.py
# Not really for beginners, not really easily understood

# some opensource libraries for better profiling: vprof, pyspy