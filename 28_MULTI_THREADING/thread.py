import threading
import time

def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(2) # simulate the work
    print(f"Thread {num}: Finishing")

threads = []

for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    # print(type(thread))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join() # wait for all threads to finish!
print("All threads completed!")   

# what is gil -> global interpretor lock in python:
# at a time only one thread is allowe dto execute python bytecode
