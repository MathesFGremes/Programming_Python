"""
multiprocess basics: Process works like threading.Thread, but 
runs function call in parallel in a process instead of a thread;
locks can be used to synchronize, e.g. prints on some platforms;
starts new interpreter on windows, forks a new process on unix;
"""

import os
from multiprocessing import Process, Lock
import time

def whoami(label, lock):
    msg = '%s: name:%s, pid:%s'
    with lock:
        print(msg % (label, __name__, os.getpid()))

def whoamiSleep(label, lock):
    msg = '%s: name:%s, pid:%s'
    with lock:
        print(msg % (label, __name__, os.getpid()))
    time.sleep(3)

if __name__ == '__main__':
    lock = Lock()
    whoami('function call', lock)

    p = Process(target=whoamiSleep, args=('spawned child', lock))
    p.start()
    #p.join()
    

    for i in range(5):
        Process(target=whoami, args=(('run process %s' % i), lock)).start()
    
    #p.start()
    #p.join()

    with lock:
        print('Main process exit.')
