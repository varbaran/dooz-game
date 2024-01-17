from utils.board import print_board
from utils.game import do_turn, is_winner, game_finished

def main():
    board = []
    # in baray tolid  3 list
    for i in range(3):
        board.append([])
        # har list ra 3 ta 0 migozarad
        for j in range(3):
            board[i].append(0)
    print_board(board)
    turn = 1
    while not game_finished(board):
        do_turn(board, turn)
        if turn == 1:
            turn = 2
        else:
            turn = 1
        print_board(board)
    if is_winner(board):
        print(f"winner is {is_winner(board)}")
    else:
        print("draw")

if __name__ == '__main__':
    main()