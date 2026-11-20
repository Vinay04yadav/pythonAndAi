import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health")

async def fetch_orders():
    await asyncio.sleep(3)
    print("Order fetched")


threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(fetch_orders())


# A background thread is created using daemon=True.
# It runs independently and logs system health every second.
# Since it's a daemon thread, it won't prevent the program from exiting
# when the main program finishes.

# Meanwhile, fetch_orders() runs as an asynchronous coroutine.
# asyncio.sleep(3) suspends the coroutine without blocking the event loop.

# Both the background thread and async routine work independently.
# The thread handles background logging while asyncio manages the async task.

# When fetch_orders() finishes after 3 seconds, asyncio.run() exits and the main program ends. Since the background thread is a daemon, it is automatically stopped rather than keeping the program alive.