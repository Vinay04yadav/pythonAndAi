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