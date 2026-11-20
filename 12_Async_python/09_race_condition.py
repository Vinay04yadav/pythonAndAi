import threading

chai_stock = 0

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

threads = [threading.Thread(target=restock) for _ in range(2)]

for t in threads: 
    t.start()

for t in threads:
    t.join()

print(f"Chai stock: {chai_stock}")

# although locally python handles this thing internally and doesn't show the unpredictable output but race condition is happening here
# which thread is accessing variable, which is updating we have no idea