from time import sleep
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = Lock() # Initialize a Lock

    def update(self, name):
        name = str(name)
        print(f"Update started on Thread: {name}")
        
        # Use 'with self.lock' to ensure thread safety
        with self.lock:
            val = self.value
            val += 1
            sleep(0.1) # Simulate some work
            self.value = val
            
        print(f"Update finished on Thread: {name}")

# Create the object
my_counter = Counter()

# Use ThreadPoolExecutor correctly
with ThreadPoolExecutor(max_workers=2) as executor:
    # Submit 10 tasks to see the race condition fix in action
    for index in range(10):
        executor.submit(my_counter.update, index)

print(f"\nFinal Counter Value: {my_counter.value}")

