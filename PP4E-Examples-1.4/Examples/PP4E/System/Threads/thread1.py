"spawn threads until you type 'q'"

import _thread

def child(tid, m):
    print('Hello from thread', tid, ' m:', m)

def parent():
    i = 0
    while True:
        i += 1
        m = i**2
        value = _thread.start_new_thread(child, (i, m,))
        print(value)
        if input() == 'q': break

parent()
