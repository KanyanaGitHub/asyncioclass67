import asyncio
from random import random

async def food(arg): #1
    value = random()+1
    print(f'Microwave ({arg}): Cooking {value} second...')
    await asyncio.sleep(value) # 2: pause, another tasks can be run
    print(f'Microwave ({arg}): finish Cooking')
    return f'- {arg} is complete in {value}'

async def main():
    #create many tasks
    arg = ["rice", "noodle", "curry"]
    tasks = [asyncio.create_task(food(i)) for i in arg]
    #wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    #report results
    print(f'Commpleted task: {len(done)} ')
    for i in done:
        print(i.result())
    print(f'Uncommpleted task: {len(pending)} ')
    
asyncio.run(main())