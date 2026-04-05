def create_board():
    board = {}
    for i in range(1, 10):
        board[i] = 0
    return board

def is_position_empty(board, pos):
    return board[pos] == 0

def get_position(board, user):
    while True:
        try:
            pos = int(input(f"U{user}_Pos (1-9): "))
            if pos < 1 or pos > 9:
                print("Pos must be 1-9")
                continue
            if not is_position_empty(board, pos):
                print(f"Pos {pos} already filled")
                continue
            return pos
        except ValueError:
            print("Enter a valid number")

def get_number(used_numbers, user):
    while True:
        try:
            num = int(input(f"U{user}_Num (1-9): "))
            if num < 1 or num > 9:
                print("Num must be 1-9")
                continue
            if num in used_numbers:
                print(f"Num {num} already used")
                continue
            return num
        except ValueError:
            print("Enter a valid number")

def store_move(board, pos, num, user):
    move_string = f"U{user}_{num}"
    board[pos] = move_string
    return board

def display_board(board):
    print("\n")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("-----------")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("-----------")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("\n")

def get_number_from_move(move_string):
    if move_string == 0: 
        return 0
    parts = move_string.split("_")
    return int(parts[1])

def check_line_wins(a, b, c):
    if (a != 0 and b != 0 and c != 0):
        if (a + b + c == 15):
            return True
        else:
            return False
    return False

def check_win(board):
    nums = {pos: get_number_from_move(board[pos]) for pos in range(1, 10)}
    if check_line_wins(nums[1], nums[2], nums[3]):
        return True
    if check_line_wins(nums[4], nums[5], nums[6]):
        return True
    if check_line_wins(nums[7], nums[8], nums[9]):
        return True
    if check_line_wins(nums[1], nums[4], nums[7]):
        return True
    if check_line_wins(nums[2], nums[5], nums[8]):
        return True
    if check_line_wins(nums[3], nums[6], nums[9]):
        return True
    if check_line_wins(nums[1], nums[5], nums[9]):
        return True
    if check_line_wins(nums[3], nums[5], nums[7]):
        return True
    return False

def play_game():
    board = create_board()
    used_numbers = set()
    current_user = 1
    
    while True:
        pos = get_position(board, current_user)
        num = get_number(used_numbers, current_user)
        store_move(board, pos, num, current_user)
        used_numbers.add(num)
        display_board(board)
        if check_win(board):
            print(f"USER {current_user} WINS! \n")
            break
        if len(used_numbers) == 9:
            print("DRAW! \n")
            break
        current_user = 3 - current_user

play_game()