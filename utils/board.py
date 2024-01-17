def print_board(board: list):
    # az khat 12 main tarif kardim ke board chand
    for i in range(len(board)):
        for j in range(len(board[i])):
            # baray ine ke har bar nare khat jadid end='' (3 taro bde badbere 3 ta badi )
            print(f"{board[i][j]}\t", end='')
        print()
