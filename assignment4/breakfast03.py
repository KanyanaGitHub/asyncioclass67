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
    print('coffee: waitting......')
    await asyncio.sleep(3) # 2: pause, another tasks can be run
    print("eggs: ready")

async def main(): #1 by teacher
    start = time()
    coffee_task = asyncio.create_task(make_coffee()) #shcedule execution
    eggs_task = asyncio.create_task(fry_eggs()) #shcedule execution
    #wait for completion, both tasks are corotine
    await make_coffee #run task with await
    await fry_egg
    print(f'breakfast is ready in {time()-start} min')
    
# async def main(): #1 gather
#     start = time()
#     await asyncio.gather(make_coffee(), fry_egg())
#     print(f'breakfast is ready in {time()-start} min')
    
asyncio.run(main()) # run top-level function