def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n, solutions):
    if row == n:
        # All queens placed successfully
        solutions.append([row[:] for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0  # backtrack


def n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)

    print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
    for i, sol in enumerate(solutions, 1):
        print(f"Solution {i}:")
        print_board(sol)



n = 4
n_queens(n)

