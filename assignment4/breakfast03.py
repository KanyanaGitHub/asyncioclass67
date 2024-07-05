# Asynchronous breakfast
import asyncio
from time import sleep, time


async def make_coffee(): #1
    print("coffee: prepare ingridients")
    sleep(1)
    print('coffee: waitting......')
    await asyncio.sleep(5) # 2: pause, another tasks can be run
    print("cofee: ready")
    
async def fry_egg(): #1
    print("eggs: prepare ingridients")
    sleep(1)
    print('eggs: waitting......')
    await asyncio.sleep(3) # 2: pause, another tasks can be run
    print("eggs: ready")
    
async def toast_bread(): #1
    print("bread: prepare ingridients")
    sleep(1)
    print('bread: waitting......')
    await asyncio.sleep(3) # 2: pause, another tasks can be run
    print("bread: ready")

async def main(): #1 by teacher
    start = time()
    coffee_task = asyncio.create_task(make_coffee()) #shcedule execution
    egg_task = asyncio.create_task(fry_egg()) #shcedule execution
    bread_task = asyncio.create_task(toast_bread()) #shcedule execution
    #wait for completion, both tasks are coroutines
    await coffee_task #run task with await
    await egg_task
    await bread_task
    print(f'breakfast is ready in {time()-start} min')
    
# async def main(): #1 gather
#     start = time()
#     await asyncio.gather(make_coffee(), fry_egg(),  toast_bread())
#     print(f'breakfast is ready in {time()-start} min')
    
asyncio.run(main()) # run top-level function