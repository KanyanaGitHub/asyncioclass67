# example of gather for many coroutines in a list
import asyncio

# coroutine use for a task
async def task_coro(value):
    #report a message
    print(f'>task {value} executing')
    #sleep for moment
    await asyncio.sleep(1)
    
#coroutine used for the entry point
async def main():
    #report a meassage
    print('main starting')
    #create manny coroutines
    coros = [task_coro(i) for i in range(10)]
    #run the tasks
    await asyncio.gather(*coros)
    #report a message
    print('main done')
    
#start the asyncio program
asyncio.run(main())