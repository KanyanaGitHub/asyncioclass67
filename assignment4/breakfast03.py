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
    
async def main(): #1
    start = time()
    await asyncio.gather(make_coffee(), fry_egg())
    print(f'breakfast is ready in {time()-start} min')
    
asyncio.run(main()) # run top-level function