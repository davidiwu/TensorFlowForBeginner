'''
The principal challenge of multi-threaded applications is coordinating threads that share data or other resources. 
To that end, the threading module provides a number of synchronization primitives including locks, events, condition variables, and semaphores.

While those tools are powerful, minor design errors can result in problems that are difficult to reproduce. 
So, the preferred approach to task coordination is to concentrate all access to a resource in a single thread and then use the queue module to feed that thread with requests from other threads. 
Applications using Queue objects for inter-thread communication and coordination are easier to design, more readable, and more reliable.

'''
import threading, zipfile
import queue
import time

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of: ', self.infile)
'''
background = AsyncZip('C:\\Projects\\video integration.trc', 'C:\\Projects\\myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()  #wait for the background task to finish
print('Main program waited untill background was done.')
'''

'''
The queue module implements multi-producer, multi-consumer queues. 
It is especially useful in threaded programming when information must be exchanged safely between multiple threads. 
The Queue class in this module implements all the required locking semantics. 
It depends on the availability of thread support in Python; see the threading module.

'''
q = queue.Queue()
threads = []
def worker():
    while True:
        item = q.get()  # a thread get a item from the queue, other threads will not be able to get this item
        print('Current Thread No.:',  threading.get_ident())
        if item is None:
            break
        do_work(item)
        q.task_done()  # indicate that a formerly enqueued task is finished

def do_work(item):
    time.sleep(10)
    print(item)

for i in range(3):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

source = [22, 33, 44, 55, 66, 88, 77]

for item in source:
    q.put(item)

# block untill all tasks are done
q.join()

# stop workers
for i in range(10):
    q.put(None)
for t in threads:
    t.join()