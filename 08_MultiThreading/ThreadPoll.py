from time import sleep
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def thread_function(name):
    print("Thread {0} started".format(name))
    sleep(2)
    print("Thread {0} end".format(name))

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_function, range(0))
    executor.map(thread_function, range(1))
    executor.map(thread_function, range(2))
    executor.map(thread_function, range(4))
