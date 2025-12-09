import math

# Initialize board
board = [" " for _ in range(9)]


def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print()


def is_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if brd[condition[0]] == brd[condition[1]] == brd[condition[2]] == player:
            return True
    return False


def is_draw(brd):
    return " " not in brd


def minimax(brd, depth, is_maximizing):
    # AI = X, Human = O

    if is_winner(brd, "X"):
        return 1
    if is_winner(brd, "O"):
        return -1
    if is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, depth + 1, False)
                brd[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, depth + 1, True)
                brd[i] = " "
                best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "X"


def player_move():
    while True:
        pos = int(input("Enter position (1-9): ")) - 1
        if 0 <= pos < 9 and board[pos] == " ":
            board[pos] = "O"
            break
        print("Invalid move! Try again.")


# Game Loop
print("Tic-Tac-Toe: You (O) vs AI (X)")
print_board()

while True:
    player_move()
    print_board()
    if is_winner(board, "O"):
        print("You win! (Impossible, how did you do that?)")
        break
    if is_draw(board):
        print("It's a draw!")
        break

    print("AI is thinking...")
    ai_move()
    print_board()

    if is_winner(board, "X"):
        print("AI wins! Better luck next time.")
        break
    if is_draw(board):
        print("It's a draw!")
        break
