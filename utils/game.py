def game_finished(board: list):
    if is_winner(board) != 0:
        return True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return False
    return True

def is_winner(board: list):
    for i in range(len(board)):
        # to yek satr barabar (i) soton hay mokhtalef ra chek mikone
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return board[i][0]
    for i in range(len(board)):
        # to yek soton barabar (i) satr hay mokhtalef ra chek mikone
        if board[0][i] == board[1][i] and board[2][i] == board[0][i]:
            return board[0][i]
    # ghotr asli ra chek mikonad
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    # ghotr farei ra chek mikonad
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[1][1]
    return 0

def do_turn(board: list, turn: int):
    x = int(input("please enter row: "))
    y = int(input("please enter column: "))
    board[x][y] = turn


