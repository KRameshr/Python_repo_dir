from time import sleep
from threading import Thread

def thread_function(name):
    print("Thread {0} started".format(name))
    sleep(2)
    print("Thread {0} end".format(name))

print("Main-Started")
t = Thread(target=thread_function, args=("new",))
print("Main - Before Starting Thread")
t.start()
print("Main - waiting for Thread to finish")
t.join()
print("Main - Done")


