# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
import multiprocessing
import os
from time import sleep, ctime, time

def cooking(index) :
    cooking_time = time()
    print(f'{ctime()} Kitchen-{index} : Begin cooking...PTD {os.getpid()}')
    sleep(2)
    duration = time() - cooking_time
    print(f'{ctime()} Kitchen-{index} : Cooking done in {duration:0.2f} second!')

def kitchen(index):
    cooking(index)    
    
if __name__=="__main__" :
    # Begin of main thread
    print(f'{ctime()} Main : Start Cooking...PID {os.getpid()}')
    start_time = time()
    
    # Multi kitchens with each chef
    kitchens = list()
    for index in range(2):#จำนวนห้องครัว
        p = multiprocessing.Process(target = kitchen, args = (index, ))
        kitchens.append(p)
        #starting processes
        p.start()
        
    for index, p in enumerate(kitchens):
        # wait until processes are finish
        p.join()
        
    duration = time() - start_time
    print(f"{ctime()} Main : Finished Cooking duration in {duration:0.2f} seconds")

#process นี้ในสองห้องครัวใช้เวลากี่วินาที 2 วิ