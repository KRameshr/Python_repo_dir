from time import sleep
from threading import Thread

def thread_function(name):
    print("Thread {0} started".format(name))
    sleep(2)
    print("Thread {0} end".format(name))

threads = []

# 1. Creating and starting threads
for index in range(3):
    print("MAIN :: creating and starting a thread {0}".format(index))
    t = Thread(target=thread_function, args=(index,))
    # FIX: Append the actual thread object 't', not the number 1
    threads.append(t) 
    t.start()

# 2. Joining threads to the main program
for index, thread in enumerate(threads):
    print("MAIN :: joining thread {0}".format(index))
    # FIX: 'thread' is now the Thread object, so .join() will work
    thread.join() 
    print("MAIN :: thread {0} has finished".format(index))

print("MAIN :: All threads complete.")