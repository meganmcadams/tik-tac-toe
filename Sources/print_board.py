def print_board(board, round):

    print("")
    print(" ## Round",round,"##")

    i = 0
    print("  ",board[i],"|",board[i + 1],"|",board[i + 2],"")
    print("  ---+---+---")
    i += 3
    print("  ",board[i],"|",board[i + 1],"|",board[i + 2],"")
    print("  ---+---+---")
    i += 3
    print("  ",board[i],"|",board[i + 1],"|",board[i + 2],"")
    print("")