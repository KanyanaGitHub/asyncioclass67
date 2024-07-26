import time
import asyncio

my_computer_time = 0.1
opponents_computer_time = 0.5
opponents = 24
move_pairs = 30

async def main(x):
    # Loops 30 time to simulate both players making a save
    borad_start_time = time.perf_counter()
    for i in range(move_pairs):
        #print(f"BOARD-{x+1} {i+1} Judit thinking of making a move.")
        time.sleep(my_computer_time)
        print(f"BOARD-{x+1} {i+1} Judit making a move.")
        #print(f"BOARD-{x+1} {i+1} Oponent thinking of making a move.")
        await asyncio.sleep(opponents_computer_time)
        print(f"BOARD-{x+1} {i+1} Opponent making a move.")
    print(f'BOARD-{x+1} >>>>>>>>>>>>>>>>> Finshed move in {round(time.perf_counter() - borad_start_time)}')
    return round(time.perf_counter() - borad_start_time)

async def async_io():
    task = []
    for i in range(opponents):
        task += [main(i)]
    await asyncio.gather(*task)
    print(f"Board exhibition finished in {round(time.perf_counter() - start_time)} sec.")
    
if __name__=="__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finish in {round(time.perf_counter() - start_time)} sec.")