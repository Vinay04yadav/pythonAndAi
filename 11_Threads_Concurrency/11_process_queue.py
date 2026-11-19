# The problem with multiprocessing is that the memory is not shared among processes
# To fix this we use queue 

from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("masala chai is ready")

if __name__ == "__main__":
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue, ))

    p.start()
    p.join()
    print(queue.get()) # If you notice we are checking the value inside queue, and we have put the value through multiprocessing (another process), so we are able to access the data basically. (sharing memory in a way)