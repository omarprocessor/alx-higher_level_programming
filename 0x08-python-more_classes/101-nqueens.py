#!/usr/bin/python3
import sys


def print_usage_and_exit():
    """Print usage and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """Utilize backtracking to solve the N-Queens problem."""
    if col >= N:
        # Found a solution, store it
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1  # Place queen
            solve_nqueens_util(board, col + 1, N, solutions)
            board[i][col] = 0  # Remove queen (backtrack)


def solve_nqueens(N):
    """Solve the N-Queens problem and print all solutions."""
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
