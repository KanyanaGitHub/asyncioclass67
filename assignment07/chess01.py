import time

my_computer_time = 0.1
opponents_computer_time = 0.5
opponents = 3
move_pairs = 30

def game(x):
    # Loops 30 time to simulate both players making a save
    borad_start_time = time.perf_counter()
    for i in range(move_pairs):
        #print(f"BOARD-{x+1} {i+1} Judit thinking of making a move.")
        time.sleep(my_computer_time)
        print(f"BOARD-{x+1} {i+1} Judit making a move.")
        #print(f"BOARD-{x+1} {i+1} Oponent thinking of making a move.")
        time.sleep(opponents_computer_time)
        print(f"BOARD-{x+1} {i+1} Opponent making a move.")
    print(f'BOARD-{x+1} >>>>>>>>>>>>>>>>> Finshed move in {round(time.perf_counter() - borad_start_time)}')
    return round(time.perf_counter() - borad_start_time)
    
if __name__=="__main__":
    start_time = time.perf_counter()
    board_time = 0
    for board in range(opponents):
        board_time += game(board)
    print(f"Board exhibition finished in {board_time} sec.")
    print(f"Finish in {round(time.perf_counter() - start_time)} sec.")