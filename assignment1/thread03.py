# extending the Thread class
from time import sleep, ctime
from threading import Thread

# custom thread class
class CutomThread(Thread):
    #override the run funtion
    def run(self):
        # block for a moment
        sleep(1)
        # display a message
        print(f'{ctime()} This is coming from another thread')

# creat thread
thread = CutomThread()
#start the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waitting for the thread to finish')
thread.join()      