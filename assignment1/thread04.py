# extending the Thread class and return values
from time import sleep, ctime
from threading import Thread

# custom thread class
class CustomThread(Thread):
    # override the run funtion
    def run(self):
        # block for a moment
        sleep(1)
        # display a message
        print(f'{ctime()} This is coming from another thread')
        # store return value
        self.value = 99
        
# create the thread        
thread = CustomThread()
# strat the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waitting for the thread to finish')
thread.join()
# get the value returned from run
value = thread.value
print (f'{ctime()} Got: {value}')